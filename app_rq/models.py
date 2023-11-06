from django.db import models
class Quote(models.Model):
    author=models.TextField()
    quote=models.TextField()
    image_url=models.TextField()
class Topics(models.Model):
    Topics=models.CharField(max_length=50000) 
class Authors(models.Model):
    Authors=models.CharField(max_length=50000) 
class Collections(models.Model):
    Collections=models.CharField(max_length=50000)
class Featured(models.Model):
    featured=models.CharField(max_length=50000)
          