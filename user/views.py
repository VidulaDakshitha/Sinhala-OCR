import ast

import bcrypt
from django.db.models import Q
from django.shortcuts import render
from rest_framework import views
import datetime
from _config.encription_handler.request_response_encriptor import decrypt_request
from .models import User
from _config.response_formaters.merchant_response_formatter import custom_response_formatter
from _config.response_configs.merchant_responses import responses
from _config.response_formaters import merchant_response_formatter
from _config.response_configs import merchant_responses
from merchant.models import Merchant
from rest_framework_simplejwt.tokens import RefreshToken
from _config.utils import date_time
from django.db import transaction
# Create your views here.
class LoginView(views.APIView):
    def post(self, request, *args):
        try:
            #request_data = decrypt_request(request.data)
            request_data = request.data

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if 'email' not in request_data or 'password' not in request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)

            data = request_data
            email = data["email"]
            password = data["password"].encode("utf8")

            try:
                user = User.objects.get(email=email, is_user=True, is_delete=False)
                try:
                    merchant = Merchant.objects.get(user_id=user.id, user_id__is_delete=False)
                except Merchant.DoesNotExist:
                    return merchant_response_formatter.custom_response_formatter({
                        "status": merchant_responses.responses['user_not_found']['code'],
                        "message": merchant_responses.responses['user_not_found']['message_en']
                    }, 200, is_encryption=True)

            except User.DoesNotExist:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['user_not_found']['code'],
                    "message": merchant_responses.responses['user_not_found']['message_en']
                }, 200, is_encryption=False)
            if user:
                if user.is_active:
                    usr_password = ast.literal_eval(user.password)
                    # user_password = ast.literal_eval()
                    if bcrypt.checkpw(password, usr_password):
                        last_login = user.last_login

                        if user.is_verified:
                            refresh = RefreshToken.for_user(user)
                            refresh_token = str(refresh)

                            access_token = str(refresh.access_token)
                            user.login_attempts = 0
                            user.last_login = date_time.get_formatted_current_time()

                            user.save()

                            data = {
                                "refresh_token": refresh_token,
                                "access_token": access_token,
                                "is_verified": 1 if user.is_verified else 0,
                                "user": {
                                    "tranding_name": merchant.trading_name if merchant.trading_name else '',
                                    "email": user.email if user.email else '',
                                    "phone_number": user.phone_no if user.phone_no else '',
                                    "user_id": merchant.user_id if merchant.user_id else '',
                                    "is_merchant": 1 if user.is_merchant else 0,

                                },

                            }
                            return merchant_response_formatter.custom_response_formatter({
                                "status": merchant_responses.responses['success']['code'],
                                "message": merchant_responses.responses['success']['message_en'],
                                "data": data,
                            }, 200, is_encryption=False)

                        else:
                            return merchant_response_formatter.custom_response_formatter({
                                "status": merchant_responses.responses['not_verify']['code'],
                                "message": merchant_responses.responses['not_verify']['message_en']
                            }, 200, is_encryption=False)
                    else:
                        if user.login_attempts:
                            login_attempts = int(user.login_attempts)
                        else:
                            login_attempts = 0

                        login_attempts = login_attempts + 1

                        user.login_attempts = login_attempts

                        if login_attempts > 4:
                            user.is_active = False
                            user.activation_description = "Reached maximum login attempts"

                        user.save()
                        return merchant_response_formatter.custom_response_formatter({
                            "status": merchant_responses.responses['invalid_user_credentials']['code'],
                            "message": merchant_responses.responses['invalid_user_credentials']['message_en']
                        }, 200, is_encryption=False)
                else:
                    return merchant_response_formatter.custom_response_formatter({
                        "status": merchant_responses.responses['user_locked']['code'],
                        "message": merchant_responses.responses['user_locked']['message_en']
                    }, 200, is_encryption=False)
        except Exception as ex:
            print('Error: MERCHANT_LOGIN: merchant login error: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class ResetPassword(views.APIView):

    def saltSecret(self):
        return bcrypt.gensalt()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:

            request_data = request.data

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if ('user_id' not in request_data or 'token' not in request_data or
                    'new_password' not in request_data or 'confirm_password' not in request_data):
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)

            data = request_data

            try:
                user = User.objects.get(~Q(is_verified=1), id=data['user_id'], is_active=1)
                if user.reset_token_expire_date:
                    expire_date = datetime.datetime.strptime(user.reset_token_expire_date,
                                                             "%Y-%m-%d %H:%M")
                    current_date = datetime.datetime.strptime(date_time.get_formatted_current_time(),
                                                              "%Y-%m-%d %H:%M")
                    if current_date > expire_date:
                        return merchant_response_formatter.custom_response_formatter({
                            "status": merchant_responses.responses['invalid_verification_token']['code'],
                            "message": merchant_responses.responses['invalid_verification_token']['message_en']
                        }, 200, is_encryption=False)
                else:
                    return merchant_response_formatter.custom_response_formatter({
                        "status": merchant_responses.responses['invalid_verification_token']['code'],
                        "message": merchant_responses.responses['invalid_verification_token']['message_en']
                    }, 200, is_encryption=False)


            except User.DoesNotExist:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['invalid_user_state']['code'],
                    "message": merchant_responses.responses['invalid_user_state']['message_en']
                }, 200, is_encryption=False)

            try:
                if user:
                    if user.reset_token == data['token']:
                        if data['new_password'] == data['confirm_password']:

                            salt = self.saltSecret()
                            password = bcrypt.hashpw(data['new_password'].encode("utf8"), salt)
                            user.password = password
                            user.is_verified = True
                            user.save()
                            return merchant_response_formatter.custom_response_formatter({
                                "status": merchant_responses.responses['success']['code'],
                                "message": merchant_responses.responses['success']['message_en']
                            }, 200, is_encryption=False)

                        else:
                            return merchant_response_formatter.custom_response_formatter({
                                "status": merchant_responses.responses['password_mis_match']['code'],
                                "message": merchant_responses.responses['password_mis_match']['message_en']
                            }, 200, is_encryption=False)
                    else:
                        return merchant_response_formatter.custom_response_formatter({
                            "status": merchant_responses.responses['invalid_verification_token']['code'],
                            "message": merchant_responses.responses['invalid_verification_token']['message_en']
                        }, 200, is_encryption=False)

            except User.DoesNotExist:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['invalid_user_state']['code'],
                    "message": merchant_responses.responses['invalid_user_state']['message_en']
                }, 200, is_encryption=False)

        except Exception as ex:
            transaction.set_rollback(True)
            print('Error: RESET NEW PASSWORD: password reset error: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)




