from django.db import models

# Create your models here

class Student(models.Model):
    name = models.CharField('Name', max_length=256)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return self.name

