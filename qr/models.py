from __future__ import unicode_literals

from django.db import models
import qrcode
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class File(models.Model):
    name = models.CharField(max_length=100)
    is_signed = models.BooleanField(default=False)
    #qr_code_path = models.ImageField(upload_to='qr/')  # TODO need to add width/height
    created_at = models.DateTimeField(auto_now_add=True)
    signed_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        add = not self.pk
        super(File, self).save(*args, **kwargs)

        if add:
            qr_img = qrcode.make('http://127.0.0.1:8000/file/'+str(self.pk))
            qr_img.save('static/'+str(self.pk)+'.png')

            kwargs['force_insert'] = False # create() uses this, which causes error.
            super(File, self).save(*args, **kwargs)



