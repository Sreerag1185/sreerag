# Generated by Django 4.2.5 on 2023-10-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='sample', upload_to='gallery'),
            preserve_default=False,
        ),
    ]