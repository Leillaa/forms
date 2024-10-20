from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from survey.models import Answer, Survey
from questionnaire.models import Question, Questionnaire, Point, HeaderCloumn


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all___'

    def create(self, data):
        Survey.objects.create(
            questionnaire=data['questionnaire']
        )
        return Response(serializers)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
    
    def validate(self, data):
        survey = data['survey']
        if not survey:
            survey = Survey.objects.get_or_create(questionnaire=data['questionnaire'])
        question = data['question']
        if not question:
            raise serializers.ValidationError('Нет опроса')
        return super().validate(data)
    
    def create(self, validated_data):
        answer = Answer.objects.create(**validated_data)
        return answer



class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'
    

class QuestionSerializer(serializers.ModelSerializer):
    """Вывод вопроса"""
    class Meta:
        model = Question
        fields = '__all__'


class HeadersSerializer(serializers.ModelSerializer):
    """Отображение заголовков столбцов в таблице рейтинга"""
    class Meta:
        model = HeaderCloumn
        fields = ('name', 'num_col')


class PointSerializers(serializers.ModelSerializer):
    """Поддерживает метод list & retriev"""
    questions = serializers.SerializerMethodField()
    headers = serializers.SerializerMethodField()

    class Meta:
        model = Point
        fields = ('id', 'name', 'number', 'questions',
                  'headers', 'num_column', 'questionnaire')

    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionSerializer(questions, many=True).data
    
    def get_headers(self, obj):
        headers = obj.header_columns.all()
        return HeadersSerializer(headers, many=True).data

    