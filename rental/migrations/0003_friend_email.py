# Generated by Django 4.1 on 2022-09-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_belonging_owner_borrowed_owner_friend_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
