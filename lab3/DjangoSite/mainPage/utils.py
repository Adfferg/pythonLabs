from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save(commit=False)
            new_object.user = request.user
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=object)
        return render(request, self.template, context={'form': bound_form, 'object': object})

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=object)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, self.template, context={'form': bound_form, 'object': object})


class ObjectDeleteMixin:
    model = None
    template = None
    template2 = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'object': object})

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        object.delete()
        return redirect(reverse(self.template2))
