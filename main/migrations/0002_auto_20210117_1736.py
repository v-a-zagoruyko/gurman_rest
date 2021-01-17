# Generated by Django 3.1.1 on 2021-01-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'блюда'},
        ),
        migrations.AlterModelOptions(
            name='menucategory',
            options={'verbose_name': 'Тип блюда', 'verbose_name_plural': 'типы блюд'},
        ),
        migrations.AlterModelOptions(
            name='menuspecimen',
            options={'verbose_name': 'Меню', 'verbose_name_plural': 'виды меню'},
        ),
        migrations.AddField(
            model_name='menuspecimen',
            name='code',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='menuspecimen',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
    ]
