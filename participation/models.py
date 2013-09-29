from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    sunet = models.CharField(max_length=100)
    late_days = models.IntegerField(default=4)
    week1 = models.CharField(max_length=1,blank=True)
    week2 = models.CharField(max_length=1,blank=True)
    week3 = models.CharField(max_length=1,blank=True)
    week4 = models.CharField(max_length=1,blank=True)
    week5 = models.CharField(max_length=1,blank=True)
    week6 = models.CharField(max_length=1,blank=True)
    week7 = models.CharField(max_length=1,blank=True)
    week8 = models.CharField(max_length=1,blank=True)
    week9 = models.CharField(max_length=1,blank=True)
    week10 = models.CharField(max_length=1,blank=True)

    def __unicode__(self):
        return '%d: %s' % (self.id,self.sunet)
