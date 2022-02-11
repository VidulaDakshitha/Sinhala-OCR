from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import views
from rest_framework.permissions import IsAuthenticated, AllowAny

from _config.bas64_image.convertor_image import stringToImage, toRGB, GraytoRGB
from _config.permission.permissions import IsMerchant
from _config.response_formaters import merchant_response_formatter
from _config.response_configs import merchant_responses
from django.db import transaction
# Create your views here.
from _services.Communicator.File_communicator import communication, communication_answer
from _services.Data_Part_Detection.datapart_main import question_datapart_main, answer_datapart_main
from _services.Enhancement.enhancement import image_main
from _services.Grammar_checker.grammar_main import grammer_main
from _services.Spell_checker.spellchecker_main import spellchecker_main
from merchant.models import Merchant
from ocrIdentification.models import Template , Answer
from ocrIdentification.serializers import TemplateSerializer, AnswerSerializer
from user.models import User


class questionOcrIdentification(views.APIView):
    permission_classes = (IsAuthenticated, IsMerchant)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:

            if 'Authorization' not in request.headers:
                return merchant_response_formatter.custom_response_formatter({
                    "status":merchant_responses.responses['unauthorized_request']['code'],
                    "message":merchant_responses.responses["unauthorized_request"]["message_en"]
                },200,is_encryption=False)
            print(request.user.id)
            request_data = request.data
            merchant = Merchant.objects.get(user_id=request.user.id)
            user = User.objects.get(id=request.user.id)

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if 'image_url' not in request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)
            data = request_data
            Image_converted = stringToImage(data['image_url'])
            RGB_converted = toRGB(Image_converted)

            # data_image=image_main(RGB_converted)
            question_part_image = []
            question_part_image = question_datapart_main(RGB_converted)

            result=communication(question_part_image,data['name'])
            # print(communication(question_part_image,data['name']))
            Template.objects.create(
                user_id=user.id,
                merchant_id=merchant.id,
                image_url=data['image_url'],
                questions=result,
                name=data['name'],
            )

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "data": result
            }, 200, False)


        except Exception as ex:
            transaction.set_rollback(True)
            print('Error: MERCHANT SELF REGISTRATION: self registration error: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class answerOcrIdentification(views.APIView):
    permission_classes = (IsAuthenticated, IsMerchant)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            user = User.objects.get(id=request.user.id)

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if 'image_url' not in request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)
            data = request_data

            # Identification image template base64 to image convertion
            Image_converted = stringToImage(data['image_url'])
            RGB_converted = toRGB(Image_converted)

            # Template get

            get_template_image=Template.objects.get(id=data['template_id'])
            Template_Image_converted = stringToImage(get_template_image.image_url)
            RGB_converted_template = toRGB(Template_Image_converted)


            data_image = image_main(RGB_converted, RGB_converted_template)

            question_part_image = answer_datapart_main(GraytoRGB(data_image))


            question_array = get_template_image.questions.split(",")
            # list_value5 = ['මම','ඔහුව','පුදු','කළේය.']
            # data_output = spellchecker_main(list_value5)

            data_output=communication_answer(question_part_image,question_array)

            n=Answer.objects.create(
                user_id=user.id,
                template_id=request_data['template_id'],
                ans_string=data_output,
            )
            n.save()

            #
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "id": data['template_id'],
                "data": data_output
            }, 200, False)


        except Exception as ex:
            transaction.set_rollback(True)
            print('Error: OCR identification: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class answerOcrIdentificationCustom(views.APIView):
    permission_classes = (IsAuthenticated, IsMerchant)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
            user = User.objects.get(id=request.user.id)

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if 'image_url' not in request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)
            data = request_data

            # Identification image template base64 to image convertion
            Image_converted = stringToImage(data['image_url'])
            RGB_converted = toRGB(Image_converted)

            # Template get

            get_template_image=Template.objects.get(id=data['template_id'])
            Template_Image_converted = stringToImage(get_template_image.image_url)
            RGB_converted_template = toRGB(Template_Image_converted)


            data_image = image_main(RGB_converted, RGB_converted_template)

            question_part_image = answer_datapart_main(GraytoRGB(data_image))


            question_array = get_template_image.questions.split(",")
            # list_value5 = ['මම','ඔහුව','පුදු','කළේය.']
            # data_output = spellchecker_main(list_value5)

            data_output=communication_answer(question_part_image,question_array)

            n=Answer.objects.create(
                user_id=user.id,
                template_id=request_data['template_id'],
                ans_string=data_output,
            )
            n.save()

            #
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "id": data['template_id'],
                "data": n.id,
                "fname":get_template_image.name
            }, 200, False)


        except Exception as ex:
            transaction.set_rollback(True)
            print('Error: OCR identification: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class grammarDetection(views.APIView):
    permission_classes = (IsAuthenticated, IsMerchant)
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data

            if not request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['decryption_error']['code'],
                    "message": merchant_responses.responses['decryption_error']['message_en']
                }, 200, is_encryption=False)

            if 'check_string' not in request_data:
                return merchant_response_formatter.custom_response_formatter({
                    "status": merchant_responses.responses['incomplete_required_fields']['code'],
                    "message": merchant_responses.responses['incomplete_required_fields']['message_en']
                }, 200, is_encryption=False)

            result_Array = grammer_main(request_data['check_string'])

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "data": result_Array
            }, 200, False)


        except Exception as ex:
            transaction.set_rollback(True)
            print('Grammar detection: ', ex)

            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class TemplateData(views.APIView):
    permission_classes = (IsAuthenticated, IsMerchant)

    def get(self,request, *args, **kwargs):
        try:

            template_data=Template.objects.values_list('id','image_url','questions','name').filter(user_id=request.user.id).all().order_by('id')
            serialized_data=TemplateSerializer(template_data,many=True)
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "data": serialized_data.data
            }, 200, False)

        except Exception as ex:
            print(ex)
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)


class trainAnswer(views.APIView):
    # permission_classes = (IsAuthenticated, IsMerchant)
    def get(self,request, *args, **kwargs):
        try:
            template_id=request.GET.get('template_id')
            answer_data=Answer.objects.values_list('id','ans_string').get(id=template_id)
            serialized_data=AnswerSerializer(answer_data,many=False)
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['success']['code'],
                "message": merchant_responses.responses["success"]["message_en"],
                "data": serialized_data.data
            }, 200, False)

        except Exception as ex:
            print(ex)
            return merchant_response_formatter.custom_response_formatter({
                "status": merchant_responses.responses['internal_server_error']['code'],
                "message": merchant_responses.responses['internal_server_error']['message_en']
            }, 200, is_encryption=False)



# class TrainAnswer(views.APIView):
#     permission_classes = (IsAuthenticated, IsMerchant)
#
#     def get(self,request, *args, **kwargs):
#         try:
#             template_data = Template.objects.values_list('id', 'image_url', 'questions', 'name').filter(
#                 user_id=request.user.id).all().order_by('id')
#             serialized_data = TemplateSerializer(template_data, many=True)
#             return merchant_response_formatter.custom_response_formatter({
#                 "status": merchant_responses.responses['success']['code'],
#                 "message": merchant_responses.responses["success"]["message_en"],
#                 "data": serialized_data.data
#             }, 200, False)
#
#         except Exception as ex:
#             print(ex)
#             return merchant_response_formatter.custom_response_formatter({
#                 "status": merchant_responses.responses['internal_server_error']['code'],
#                 "message": merchant_responses.responses['internal_server_error']['message_en']
#             }, 200, is_encryption=False)
