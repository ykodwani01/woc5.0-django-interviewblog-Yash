# Generated by Django 3.2.16 on 2023-01-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_auto_20230124_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='job_offer',
            field=models.CharField(choices=[('Summer Intern', 'Summer Intern'), ('Job', 'Job'), ('PPO', 'PPO'), ('Winter Intern', 'Winter Intern')], default=1, max_length=100),
        ),
    ]
