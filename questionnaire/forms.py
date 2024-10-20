from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import Point, Question
from survey.forms import AnswerForm


class ElementInLineFormSet(BaseInlineFormSet):

    def clean(self):
        """Проверка заполнености полей."""
        super(ElementInLineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
                   for cleaned_data in self.cleaned_data):
            raise forms.ValidationError(
                'Нужно добавить хоть один элемент'
            )

class QuestionForm(forms.ModelForm):
    answer = forms.CharField(label='Ответ')

    class Meta:
        model = Question
        fields = ('answer',)

PointFormSet = inlineformset_factory(
    Point,
    Question,
    form=QuestionForm,
    extra=0
)