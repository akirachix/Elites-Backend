# Generated by Django 4.2.13 on 2024-07-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_name', models.CharField(max_length=20)),
                ('factory_email', models.EmailField(max_length=254)),
                ('factory_location', models.CharField(max_length=20)),
            ],
        ),
    ]
