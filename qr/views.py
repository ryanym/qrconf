from django.shortcuts import render
from django.http import HttpResponse
from .models import File
# Create your views here.


def index(request):

    return HttpResponse("qr app home")


def display(request, file_id):

    file_ = File.objects.get(pk=file_id)
    context = {
        'file': file_
    }
    return render(request,'qr/qrcode.html',context)
