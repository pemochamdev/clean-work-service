from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Service(models.Model):
    '''Model definition for Service.'''
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    image = models.ImageField(upload_to='clean-work')
    description = models.TextField()
    amount = models.IntegerField()
    hours = models.IntegerField()


    class Meta:
        '''Meta definition for Service.'''

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
    


class PhotoGallery(models.Model):
    '''Model definition for PhotoGallery.'''

    service =models.ForeignKey(Service, on_delete=models.CASCADE, related_name='photogallery')
    image = models.ImageField(upload_to='photo-gallery')


    class Meta:
        '''Meta definition for PhotoGallery.'''

        verbose_name = 'PhotoGallery'
        verbose_name_plural = 'PhotoGallerys'

    def __str__(self):
        return self.service.name