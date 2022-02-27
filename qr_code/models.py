from django.db import models
import qr_code
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=200)
    qrcode = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)
    def save(self,*args, **kwargs):
        qrcode_img = qr_code.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code_{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(fname, File(buffer), save=File)
        canvas.close()
        super().save(*args, **kwargs)
