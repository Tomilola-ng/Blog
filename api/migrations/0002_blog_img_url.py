# Generated by Django 4.2.5 on 2023-09-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img_url',
            field=models.CharField(default='istockphoto.com/beards.jpg', max_length=225),
        ),
    ]
