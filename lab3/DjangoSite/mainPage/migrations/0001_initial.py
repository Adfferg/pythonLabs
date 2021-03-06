# Generated by Django 3.0.5 on 2020-05-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=50, unique=True)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('name_of_user', models.ManyToManyField(related_name='user_posts', to='mainPage.Users')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='mainPage.Tag')),
            ],
        ),
    ]
