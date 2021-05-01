# Generated by Django 3.1.5 on 2021-05-01 15:50

import asset.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=asset.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
            ],
            options={
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
        ),
    ]
