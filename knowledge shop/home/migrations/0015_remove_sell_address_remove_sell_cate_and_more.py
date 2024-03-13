# Generated by Django 4.1.4 on 2023-09-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_sell_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell',
            name='address',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='cate',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='prod_id',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='year',
        ),
        migrations.AddField(
            model_name='sell',
            name='desc',
            field=models.TextField(default='I want to sell book'),
        ),
        migrations.AddField(
            model_name='sell',
            name='email',
            field=models.CharField(default='book@gmial.com', max_length=122),
        ),
        migrations.AddField(
            model_name='sell',
            name='name',
            field=models.CharField(default='I want to sell book', max_length=122),
        ),
        migrations.AlterField(
            model_name='sell',
            name='phone',
            field=models.CharField(default='65', max_length=12),
        ),
    ]