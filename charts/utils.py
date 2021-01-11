import os
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadTo:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, filename):
        upload_to = f"static/{instance.__class__.__name__}/{instance.slug}/{self.name}"
        ext = filename.split('.')[-1]
        if instance.pk:
            filename = f'{instance.pk}_{instance.slug}.{ext}'
        else:
            pass
        return os.path.join(upload_to, filename)