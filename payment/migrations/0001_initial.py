# Generated by Django 2.2.12 on 2024-07-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', models.PositiveIntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_deducted', models.DecimalField(decimal_places=2, max_digits=6)),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
    ]