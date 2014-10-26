from django.db import models

class GuestLog(models.Model):
  ip_address = models.CharField('IP Address', max_length=45)
  access_date = models.DateTimeField('Access Time')
  f_name = models.CharField('First Name', max_length=30)
  l_name = models.CharField('Last Name', max_length=30)
  favorite_dino = models.CharField('Favorite Dinosaur', max_length=50)
  def __str__(self):
    return f_name.text + ' ' + l_name.text
# Create your models here.
