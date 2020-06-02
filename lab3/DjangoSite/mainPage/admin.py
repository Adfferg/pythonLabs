from django.contrib import admin

# Register your models here.
from mainPage.models import Post, Tag, Users

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Users)
