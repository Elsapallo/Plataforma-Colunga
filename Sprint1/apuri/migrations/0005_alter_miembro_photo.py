# Generated by Django 3.2.2 on 2021-06-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuri', '0004_alter_miembro_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='photo',
            field=models.ImageField(null=True, upload_to='perfil'),
        ),
    ]
