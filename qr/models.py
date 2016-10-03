from __future__ import unicode_literals

from django.db import models
import qrcode
import StringIO
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class File(models.Model):
    name = models.CharField(max_length=100)
    is_signed = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qrcode', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    signed_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('qr.views.display', args=(str(self.pk)))


    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        )
        qr.add_data(self.get_absolute_url())
        qr.make(fit=True)

        img = qr.make_image()

        buffer = StringIO.StringIO()
        img.save(buffer)
        file_name = 'qr-%s.png' % self.pk
        file_buffer = InMemoryUploadedFile(
            buffer, None, file_name, 'image/png', buffer.len, None)
        self.qr_code.save(file_name, file_buffer)

    def save(self, *args, **kwargs):
        add = not self.pk
        super(File, self).save(*args, **kwargs)

        if add:
            self.generate_qrcode()
            kwargs['force_insert'] = False # create() uses this, which causes error.
            super(File, self).save(*args, **kwargs)



