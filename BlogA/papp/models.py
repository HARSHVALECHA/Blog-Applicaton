from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class info(models.Model):
    title=models.CharField(max_length=10)
    slug=models.SlugField(max_length=250,null=True)
    description=models.TextField(max_length=50)
    pos=models.FileField(upload_to = 'pic',null=True)
    date_created=models.DateTimeField(auto_now=True,null=True)
    created_by=models.ForeignKey(User,null=True)
    def __unicode__(self):
        return self.title
class comment(models.Model):
    post = models.ForeignKey(info, blank=True, null=True)
    cmt_user = models.ForeignKey(User, blank=True, null=True)
    user_cmt = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.user_cmt

class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50,null=True,blank=True)
    
    pic = models.FileField(upload_to='images',blank=True,null=True)

    class Meta:
        db_table = 'auth_profile'
        
    def __unicode__(self):
        return self.location

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

