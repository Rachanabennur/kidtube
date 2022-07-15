# Generated by Django 4.0.4 on 2022-06-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('vid', models.FileField(upload_to='')),
                ('category', models.CharField(default='', max_length=100)),
                ('tags', models.BooleanField(default=False)),
                ('url', models.URLField(default='')),
                ('comments', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]