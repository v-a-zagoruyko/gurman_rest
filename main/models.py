from django.db import models

class MenuSpecimen(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class MenuKind(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Menu(models.Model):
    specimen = models.ForeignKey(MenuSpecimen, on_delete=models.CASCADE, blank=True, null=True, related_name='specimen')
    kind = models.ForeignKey(MenuKind, on_delete=models.CASCADE, blank=True, null=True, related_name='kind')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)
    cost = models.PositiveSmallIntegerField(blank=True, null=True,)
    sale = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.CharField(max_length=16, blank=True, null=True)
    image = models.ImageField(upload_to='menu', blank=True, null=True)

    def __str__(self):
        return self.title
