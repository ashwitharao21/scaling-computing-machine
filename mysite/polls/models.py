from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Employee(models.Model):
    empId = models.IntegerField()
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=200)