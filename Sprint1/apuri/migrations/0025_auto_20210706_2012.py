# Generated by Django 3.1.7 on 2021-07-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0024_auto_20210706_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='tipo',
            field=models.CharField(max_length=200, null=True, verbose_name='Tipo anuncio'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='desc',
            field=models.TextField(verbose_name='Descripción anuncio'),
        ),
    ]