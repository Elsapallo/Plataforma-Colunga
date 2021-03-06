# Generated by Django 3.1.7 on 2021-06-22 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0016_miembro_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='rol',
            field=models.CharField(choices=[('Usuario', 'Usuario'), ('Administrador', 'Administrador')], default='Usuario', max_length=40, verbose_name='Rol'),
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='Anuncios', verbose_name='Foto de Anuncio')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuri.miembro')),
            ],
        ),
    ]
