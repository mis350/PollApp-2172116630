from django.db import models

# Create your models here.
class Poll(models.Model):
  STATUS = (
    (0,"Draft"),
    (1,"Publish")
  )
  title = models.CharField(max_length=100, unique=True)
  question = models.CharField(max_length=100, unique=True)
  active_until = models.DateTimeField(auto_now_add=True)
  id = models.BigAutoField(primary_key=True)
  status = models.IntegerField(choices=STATUS, default=0)
  
class Options(models.Model):
  title = models.CharField(max_length=100, unique=True)
 
poll = models.ForeignKey("Poll",on_delete=models.CASCADE)

class Response(models.Model):
  name = models.CharField(max_length=100, unique=True)
  response_time = models.DateTimeField(auto_now_add=True)
  default=''
  Options = models.ForeignKey("Options",default=None,on_delete=models.CASCADE)