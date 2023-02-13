from django.shortcuts import render
from .forms import ImageInfoForm
from .models import ImageInfo
# Create your views here.
def home(request):
    if request.method=="POST":
        form = ImageInfoForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
    form = ImageInfoForm()
    img = ImageInfo.objects.all()
    return render(request, 'app/home.html', {'img':img ,'form':form})