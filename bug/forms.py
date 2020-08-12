from django import forms
from .models import UploadImages, UploadTarget
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib import messages

class AnalizarImagenes(forms.ModelForm):

    class Meta:
        model = UploadImages
        fields = '__all__'

class CargarTarget(forms.ModelForm):
    class Meta:
        model = UploadTarget
        fields = '__all__'