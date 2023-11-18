# Generated by Django 4.2.5 on 2023-11-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(choices=[('commerce', 'Commerce'), ('science', 'Science')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('purpose', models.CharField(choices=[('enquiry', 'Enquiry'), ('place_order', 'Place Order'), ('return', 'Return')], max_length=20)),
                ('materials_provided', models.ManyToManyField(blank=True, to='credentials.material')),
            ],
        ),
    ]
