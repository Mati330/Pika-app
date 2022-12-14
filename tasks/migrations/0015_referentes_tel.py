# Generated by Django 3.2.16 on 2022-12-20 07:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0014_referentes_redes_referentes_seginf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referentes_tel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_error_teluno', models.ImageField(blank=True, null=True, upload_to='Referentes_tel/')),
                ('imagen_error_teldos', models.ImageField(blank=True, null=True, upload_to='Referentes_tel/')),
                ('imagen_error_teltres', models.ImageField(blank=True, null=True, upload_to='Referentes_tel/')),
                ('area_principal', models.CharField(max_length=50, null=True)),
                ('nombre_referente', models.CharField(max_length=50, null=True)),
                ('nombres_integrantes', models.CharField(max_length=60, null=True)),
                ('apps', models.CharField(max_length=500, null=True)),
                ('titulo_error', models.CharField(max_length=50, null=True)),
                ('descripcion_error', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha_error', models.DateField()),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
