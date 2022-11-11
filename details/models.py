from django.db import models

class Student_details(models.Model):
    name=models.CharField(max_length=300)
    roll_no=models.IntegerField()
    section= models.CharField(max_length=40)
    age=models.IntegerField()

