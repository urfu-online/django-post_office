# Generated by Django 1.11.3 on 2017-07-31 11:42
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('post_office', '0006_attachment_mimetype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'ordering': ['name'], 'verbose_name': 'Email Template', 'verbose_name_plural': 'Email Templates'},
        ),
    ]
