# Generated by Django 4.1.4 on 2023-01-28 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogFinal', '0003_publicacion_autor_alter_publicacion_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publicacion',
        ),
    ]
