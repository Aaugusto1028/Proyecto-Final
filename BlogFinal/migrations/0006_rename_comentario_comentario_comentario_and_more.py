# Generated by Django 4.1.4 on 2023-02-03 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogFinal', '0005_publicacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='Comentario',
            new_name='comentario',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Fecha',
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
