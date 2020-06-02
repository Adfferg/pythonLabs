from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from mainPage.models import Tag, Post, Users


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('"{}" уже есть'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class UserForm(forms.Form):
    User_Name = forms.CharField(max_length=50)
    First_Name = forms.CharField(max_length=50)
    Last_Name = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50)

    User_Name.widget.attrs.update({'class': 'form-control'})
    First_Name.widget.attrs.update({'class': 'form-control'})
    Last_Name.widget.attrs.update({'class': 'form-control'})
    Email.widget.attrs.update({'class': 'form-control'})
    Password.widget.attrs.update({'class': 'form-control'})

    def clean_user(self):
        new_user = self.cleaned_data['User_Name']
        if User.objects.filter(username__iexact=new_user).count():
            raise ValidationError('Пользователь "{}" уже есть'.format(new_user))
        return new_user

    def save(self):
        user = User.objects.create_user(self.cleaned_data['User_Name'], self.cleaned_data['Email'],
                                        self.cleaned_data['Password'])
        user.first_name = self.cleaned_data['First_Name']
        user.last_name = self.cleaned_data['Last_Name']
        new_user = Users()
        new_user.User_Name = self.cleaned_data['User_Name']
        new_user.First_Name = self.cleaned_data['First_Name']
        new_user.Last_Name = self.cleaned_data['Last_Name']
        new_user.Email = self.cleaned_data['Email']
        user.save()
        new_user.save()
