# Generated by Django 4.1.4 on 2023-01-28 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogFinal', '0002_alter_publicacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(default='imagen', upload_to='publicaciones/'),
        ),
    ]
