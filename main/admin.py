from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(MenuSpecimen)
class MenuSpecimenAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(MenuKind)
class MenuKindAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />'.format(obj.image.url))

    image_tag.short_description = ''

    list_display = ('image_tag', 'specimen', 'kind', 'title', 'description' )
