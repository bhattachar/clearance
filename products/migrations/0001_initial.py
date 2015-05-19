# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('url', models.URLField()),
                ('description', models.TextField(default=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120, null=True, blank=True)),
                ('price', models.CharField(max_length=120)),
                ('clearance', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=b'products/images/')),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_url', models.URLField(default=b'www.wowclearance.com')),
                ('brand_url', models.URLField(default=b'www.wowclearance.com')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
