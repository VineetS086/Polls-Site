from django import forms
from .models import Question, Choice


class Question_Create_Form(forms.ModelForm):




    class Mera:
        model = Question
        fields = ['question_text']


class Choice_Create_Form(forms.ModelForm):




    class Mera:
        model = Choice
        fields = ['question_text']

