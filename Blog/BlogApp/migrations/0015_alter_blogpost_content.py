# Generated by Django 3.2.16 on 2023-01-30 12:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0014_bookm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
