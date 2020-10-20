from django.db import models

from datetime import datetime

class Question(models.Model):
    question_text   = models.CharField(max_length=150)
    pub_date        = models.DateTimeField('Date Created', default= datetime.now())
    votes           = models.IntegerField(default=0)


    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    votes       = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.choice_text} - {self.question}' 
    

    