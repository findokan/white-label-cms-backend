# Generated by Django 4.0.5 on 2022-06-14 19:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_base', '0003_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
