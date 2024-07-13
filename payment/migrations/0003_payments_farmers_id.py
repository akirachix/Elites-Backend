# Generated by Django 4.2.14 on 2024-07-13 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers_details', '0002_alter_farmers_details_id'),
        ('payment', '0002_alter_payments_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='farmers_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmers_details.farmers_details'),
        ),
    ]
