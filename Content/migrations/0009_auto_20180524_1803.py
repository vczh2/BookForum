# Generated by Django 2.0.5 on 2018-05-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Content', '0008_auto_20180524_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='intro',
            field=models.TextField(blank=True, max_length=128, verbose_name='展示简介'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='title',
            field=models.CharField(blank=True, max_length=128, verbose_name='展示标题'),
        ),
    ]