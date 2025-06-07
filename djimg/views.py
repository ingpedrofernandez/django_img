from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'djimg/index.html', {})


# Upload Image View
def UploadImage(request):
    if request.method=="POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(Imagename=imagename,Image=pics)
        return redirect('show')


# Image Fetching View
def ImageFetch(request):
    all_img = ImageData.objects.all()
    return render(request,"djimg/show.html",{'key1':all_img})