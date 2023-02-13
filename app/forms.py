from django import forms
from .models import ImageInfo

class ImageInfoForm(forms.ModelForm):
    class Meta:
        model = ImageInfo
        fields = '__all__'
        labels = {'photo':''}   ###remove the label form photo