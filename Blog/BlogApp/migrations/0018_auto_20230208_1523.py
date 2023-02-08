# Generated by Django 3.2.16 on 2023-02-08 09:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0017_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
