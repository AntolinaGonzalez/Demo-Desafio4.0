from django.db import models
from .utils import get_filteres_image, lookForTarget
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib import messages
# Create your models here.
ACTION_CHOICES = (
    ('NO_FILTER','no filter'),
    ('COLORIZED', 'colorized')
)
class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __string__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        #open image
        pil_img = Image.open(self.image)
        #convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filteres_image(cv_img, self.action)
        #CONVERT TO PIL IMAGE

        im_pil = Image.fromarray(img)

        #save

        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)
        super().save(*args,**kwargs)

    

class UploadImage(models.Model):
    imageToCompare = models.ImageField(upload_to='images')
    imageTarget = models.ImageField(upload_to='images')
    objetivo = models.CharField(max_length=150)

    def __string__(self):
        return str(self.objetivo)

    def save(self, *args, **kwargs):
        #open image
        imgCompare = Image.open(self.imageToCompare)
        imgTarget = Image.open(self.imageTarget)
        #convert the image to array and do some processing
        cv_compare = np.array(imgCompare)
        cv_Target = np.array(imgTarget)

        #execute the function
        img = lookForTarget(cv_compare,cv_Target)

        #CONVERT TO PIL IMAGE
        im_pil = Image.fromarray(img)

        #save

        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.imageToCompare.save(str(self.imageToCompare), ContentFile(image_png), save=False)
        super().save(*args,**kwargs)

    