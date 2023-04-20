from django.db import models

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.firstname+' '+self.lastname

