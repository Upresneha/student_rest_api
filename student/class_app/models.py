from django.db import models
from datetime import timedelta, datetime
from datetime import datetime


class stu(models.Model):
    name  = models.CharField(max_length=20)
    roll_no   = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self) -> str:
        return self.name    
    

class staff(models.Model):
    name  = models.CharField(max_length=20)
    staff_id  = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.name    