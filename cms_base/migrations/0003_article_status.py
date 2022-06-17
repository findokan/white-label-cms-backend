# Generated by Django 4.0.5 on 2022-06-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_base', '0002_tag_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('U', 'Unpublished'), ('P', 'Published')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]