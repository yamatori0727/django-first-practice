from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    return HttpResponse('<h1>Hello World!</h1>')


class HelloWorldClass(TemplateView):
    template_name = 'hello.html'

