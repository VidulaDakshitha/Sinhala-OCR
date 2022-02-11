import ast
import decimal
from decimal import Decimal

from rest_framework import serializers
from .models import Template


class TemplateSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'id': obj[0],
            'image_url': obj[1] if obj[1] else '',
            'questions': obj[2] if obj[2] else '',
            'name': obj[3] if obj[3] else '',

        }

class AnswerSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'id': obj[0],
            'ans_string': ast.literal_eval(obj[1]) if obj[1] else '',

        }

