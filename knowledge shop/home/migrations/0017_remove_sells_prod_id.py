# Generated by Django 4.1.4 on 2023-09-23 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_sells_delete_sell'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sells',
            name='prod_id',
        ),
    ]
