# Generated by Django 4.1.10 on 2023-07-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ManyToManyField(related_name='user_data', to='app.users'),
        ),
    ]
