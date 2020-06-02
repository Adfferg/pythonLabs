from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    name_of_user = models.ManyToManyField('Users', blank=False, related_name='user_posts')
    # user = models.CharField(max_length=50, db_index=True,blank=True)
    title = models.CharField(max_length=150, blank=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url',
                       kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url',
                       kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Users(models.Model):
    User_Name = models.CharField(max_length=50, unique=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', default="https://pbs.twimg.com/profile_images/1056643396507459585/-jhnJW4v_400x400.jpg", max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.User_Name)
