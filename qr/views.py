from django.shortcuts import render
from django.http import HttpResponse
from .models import File
# Create your views here.


def index(request):

    if 'conf-check' in request.POST and 'submit' in request.POST:
        file_ = File.objects.get(pk=request.POST['conf-check'])
        # print request.POST
        return HttpResponse(file_.name)

    else:
        return HttpResponse(":/")


def display(request, file_id):

    file_ = File.objects.get(pk=file_id)
    context = {
        'file': file_
    }
    return render(request, 'qr/qrcode.html', context)


def confirm(request, file_id):

    file_ = File.objects.get(pk=file_id)
    context = {
        'file': file_
    }

    return render(request, 'qr/confirm.html', context)