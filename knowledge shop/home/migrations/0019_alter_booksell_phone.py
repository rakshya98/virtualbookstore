# Generated by Django 4.1.4 on 2023-09-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_booksell_delete_sells'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksell',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
