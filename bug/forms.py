from django import forms
from .models import UploadImage

class AnalizarImagenes(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = '__all__'