# Generated by Django 3.1.7 on 2021-10-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucnitk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Status',
            field=models.CharField(default='Not Accepted', max_length=15),
        ),
    ]
