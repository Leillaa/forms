from django.contrib import admin

from .forms import ElementInLineFormSet
from .models import Survey, Answer


class AnswerInLine(admin.TabularInline):
    model = Answer
    formset = ElementInLineFormSet
    extra = 1

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'survey', 'question']
    pass

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['date', 'questionnaire']
    inlines = [AnswerInLine]
