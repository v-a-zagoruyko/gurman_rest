from django.db import models

class MenuSpecimen(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True, verbose_name='Код')
    title = models.CharField(max_length=64, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'виды меню'

class MenuCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'типы блюд'

class Menu(models.Model):
    specimen = models.ManyToManyField(MenuSpecimen, related_name='specimen', verbose_name='Меню')
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='category', verbose_name='Тип')
    title = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=512, blank=True, null=True, verbose_name='Состав')
    cost = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Цена')
    weight = models.CharField(max_length=16, blank=True, null=True, verbose_name='Вес (в граммах)')
    image = models.ImageField(upload_to='menu', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'блюда'
