from django import forms
from .models import UploadImage
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib import messages

class AnalizarImagenes(forms.ModelForm):

    class Meta:
        model = UploadImage
        fields = '__all__'