from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profils(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phon_num = models.CharField(max_length=15 , null=True , blank=True)
    addres = models.CharField(max_length=50 , null=True , blank=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save , sender=User)
def creatv_user(sender,instance,created,**kwargs):
    if created:
        Profils.objects.create(user=instance)