# Generated by Django 3.2.7 on 2021-10-14 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ucnitk', '0008_auto_20211014_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=15)),
                ('IssueType', models.CharField(choices=[('Order Taking Too Long To Be Delivered/Accepted', 'Order Taking Too Long To Be Delivered/Accepted'), ('Issue With Service Provider', 'Issue With Service Provider'), ('Order Status Says Delivered but did not recieve anything', 'Order Status Says Delivered but did not recieve anything'), ('Other', 'Other')], default='Other', max_length=160)),
                ('IssueDetails', models.CharField(choices=[('Order Taking Too Long To Be Delivered/Accepted', 'Order Taking Too Long To Be Delivered/Accepted'), ('Issue With Service Provider', 'Issue With Service Provider'), ('Order Status Says Delivered but did not recieve anything', 'Order Status Says Delivered but did not recieve anything'), ('Other', 'Other')], default='Nothing', max_length=500)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Help_Customer', to=settings.AUTH_USER_MODEL)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order', to='ucnitk.order')),
            ],
        ),
    ]