# Generated by Django 3.2.7 on 2021-10-15 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ucnitk', '0010_help_addedtime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RemoveField(
            model_name='help',
            name='AddedTime',
        ),
        migrations.RemoveField(
            model_name='help',
            name='IssueDetails',
        ),
        migrations.RemoveField(
            model_name='help',
            name='IssueType',
        ),
        migrations.RemoveField(
            model_name='help',
            name='Order',
        ),
        migrations.RemoveField(
            model_name='help',
            name='Status',
        ),
        migrations.AddField(
            model_name='help',
            name='OrderWh',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Order_Wh', to='ucnitk.order'),
        ),
    ]