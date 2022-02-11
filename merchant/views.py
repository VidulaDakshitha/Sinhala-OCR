import datetime

from django.shortcuts import render
from rest_framework import views
from _config.response_formaters import merchant_response_formatter
from _config.response_configs import merchant_responses
from django.db import transaction
from user.models import User
from merchant.models import Merchant
from _config.email.tokens import account_activation_token
from _config.utils import date_time
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# Create your views here.
class MerchantSelfRegisterView(views.APIView):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            # request_data = request.data
            print(request_data)

            if ('first_name' not in request_data or
                    'business_category' not in request_data or 'nic' not in request_data or
                    'gender' not in request_data or
                    'trading_name' not in request_data or
                    'phone_number' not in request_data or
                    'email' not in request_data):
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=True)

            data = request_data

            # check unique values
            try:
                print("came into try catch")
                User.objects.get(email=data['email'])
                print("came into try catch2")
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['duplicate_email_values']['code'],
                    "message": merchant_responses.responses['duplicate_email_values']['message_en']
                }, 200, is_encryption=False)

            except User.DoesNotExist:
                print('no duplicate email ')

            try:
                User.objects.get(phone_no=data['phone_number'])

                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['duplicate_phone_no_values']['code'],
                    "message": merchant_responses.responses['duplicate_phone_no_values']['message_en']
                }, 200, is_encryption=True)

            except User.DoesNotExist:
                print('no duplicate phone number')

            # user save
            print("save user detail no")
            user = User.objects.create(
                email=data['email'],
                phone_no=data['phone_number'],
                is_user=True,
                is_merchant=True,
                is_active=1,
                date_joined = datetime.datetime.now(),
                delete_on = datetime.datetime.now()
                # create_on=date_time.get_formatted_current_time()
            )
            print("save user detail successfully")

            # merchant save

            # 'identification'
            merchant = Merchant.objects.create(
                user_id=user.id,
                first_name=data['first_name'],
                last_name=data['last_name'],
                business_category=data['business_category'],
                trading_name=data['trading_name'],

            )
            print("save merchant detail successfully")

            subject = 'Merchant Registration'

            values = {
                'user': merchant.first_name,
                'domain': 'http://localhost:3000/#/',
                'uid': user.id,
                'email': user.email,
                'token': account_activation_token.make_token(user),

            }
            user.reset_token = values['token']
            user.reset_token_expire_date=date_time.get_token_expire_date()
            user.save()

            htmly = get_template('self_registration.html')
            html_content = htmly.render(values)
            msg = EmailMultiAlternatives(
                subject, '', "noreply@sinhalaocr.com", [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses['success']['message_en'],
                "data": user.email
            }, 200, is_encryption=False)

        except Exception as ex:
            transaction.set_rollback(True)
            print('Error: MERCHANT SELF REGISTRATION: self registration error: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": ex
            }, 200, is_encryption=False)