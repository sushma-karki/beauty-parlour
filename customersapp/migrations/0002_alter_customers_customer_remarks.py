# Generated by Django 3.2.8 on 2021-12-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_remarks',
            field=models.CharField(max_length=20),
        ),
    ]