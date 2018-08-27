from django.db import models

# Create your models here.
class CurrentApp(models.Model):
  app_name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  address = models.CharField(max_length=200)

  def __str__(self):
    return self.app_name
