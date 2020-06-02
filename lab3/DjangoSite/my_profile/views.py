from django.shortcuts import render

from mainPage.models import Users


def show_profile(request, site_user):
    this_user = Users.objects.get(User_Name__iexact=site_user);
    return render(request, 'my_profile/profile.html', context={'this_user': this_user})
