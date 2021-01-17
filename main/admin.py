from django.contrib import admin
from django.utils.html import format_html
from .models import *

admin.site.site_url = 'https://ресторан-гурман.рф'
admin.site.site_header = 'Ресторан Гурман'

@admin.register(MenuSpecimen)
class MenuSpecimenAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    def specimen_tag(self, obj):
        list_items = ''
        for specimen in obj.specimen.all():
            list_items += f'<li>{specimen}</li>'
        return format_html('<ul>{}</ul>'.format(list_items))

    specimen_tag.short_description = 'Меню'

    list_display = ('title', 'cost', 'weight', 'category', 'specimen_tag')
