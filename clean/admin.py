from django.contrib import admin

from clean.models import Service, PhotoGallery
import admin_thumbnails

# TODO: install django-admin-thumbnails
# after install : import admin_thumbnails
#in to the model admin make @admin_thumbnails.thumbnail('image)

@admin_thumbnails.thumbnail('image')
class PhotoGalleryInline(admin.TabularInline):
    '''Tabular Inline View for PhotoGallery'''

    model = PhotoGallery
    min_num = 3
    max_num = 10
    extra = 1
    #raw_id_fields = (,)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('name','amount', 'hours')    
    search_fields = ('name',)

    prepopulated_fields = {"slug": ["name"]}
    inlines = [PhotoGalleryInline]


admin.site.register(PhotoGallery)

