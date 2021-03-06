# Generated by Django 3.2.10 on 2021-12-21 20:36

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Game name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Cheese Address')),
                ('max_players', models.IntegerField(verbose_name='Max number of players')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
