from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    msg = models.CharField(max_length=100)

    def __str__(self):
        return "name :"+self.name+" email :"+self.email+" message :"+self.msg

class Register(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return "name : "+self.fname

class Notice(models.Model):
   image = models.ImageField(default="")
   desc = models.CharField(max_length=100)
   name = models.CharField(max_length=50)


   def __str__(self):
        return "name : "+self.name