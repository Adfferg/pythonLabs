# Generated by Django 3.0.5 on 2020-05-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, default='https://pbs.twimg.com/profile_images/1056643396507459585/-jhnJW4v_400x400.jpg', max_length=255, null=True, upload_to='pictures/%Y/%m/%d'),
        ),
    ]
