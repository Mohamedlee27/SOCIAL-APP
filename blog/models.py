from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,unique=True,max_length=111)
    content =  models.TextField()
    image =  models.ImageField(upload_to='post_images')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ 
                                        Transpose(),
                                        ResizeToFill(1000, 500)
                                        ],
                                      format='JPEG',
                                      options={'quality': 70})

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes',blank=True)
    tagged_users = models.ManyToManyField(User, related_name='tagged_users',blank=True)

    @property
    def total_likes(self):
        return self.likes.count()