# Generated by Django 3.1.2 on 2021-03-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210327_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=122, null=True),
        ),
    ]
