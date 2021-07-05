# Generated by Django 3.1.7 on 2021-07-03 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0019_auto_20210628_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='hfin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='hini',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuri.miembro', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='Tipo anuncio'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]