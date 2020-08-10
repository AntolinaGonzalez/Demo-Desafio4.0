from django.db import models
from django.db import models
from .utils import lookForTarget,lookForTargetMessage
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib import messages

# Create your models here.
class UploadImage(models.Model):
    imageToCompare = models.ImageField(upload_to='images')
    imageTarget = models.ImageField(upload_to='images')
    objetivo = models.CharField(max_length=150)

    def __string__(self):
        return str(self.objetivo)
    
    def getResult(self):
        imgCompare = Image.open(self.imageToCompare)
        imgTarget = Image.open(self.imageTarget)
        #convert the image to array and do some processing
        cv_compare = np.array(imgCompare)
        cv_Target = np.array(imgTarget)

        #execute the function
        img = lookForTargetMessage(cv_compare,cv_Target,'objectivo')
        
        return img 
    
    

    