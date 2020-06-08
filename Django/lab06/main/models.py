from django.db import models

# Create your models here.

class Todo(models.Model):
    date = models.DateField(verbose_name="날짜")
    title = models.CharField(max_length=150, verbose_name="제목")
    text = models.TextField(verbose_name="할 일")