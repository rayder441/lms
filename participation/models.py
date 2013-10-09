from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    sunet = models.CharField(max_length=100,null=True)
    late_days = models.IntegerField(default=4)
    week1 = models.CharField(max_length=1,blank=True,null=True)
    week2 = models.CharField(max_length=1,blank=True,null=True)
    week3 = models.CharField(max_length=1,blank=True,null=True)
    week4 = models.CharField(max_length=1,blank=True,null=True)
    week5 = models.CharField(max_length=1,blank=True,null=True)
    week6 = models.CharField(max_length=1,blank=True,null=True)
    week7 = models.CharField(max_length=1,blank=True,null=True)
    week8 = models.CharField(max_length=1,blank=True,null=True)
    week9 = models.CharField(max_length=1,blank=True,null=True)
    week10 = models.CharField(max_length=1,blank=True,null=True)

    def __unicode__(self):
        return '%d: %s' % (self.id,self.sunet)
