# Generated by Django 4.0.4 on 2022-05-19 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_feed_img_alter_feed_vid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Videos',
        ),
    ]