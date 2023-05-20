# Generated by Django 3.2.17 on 2023-05-20 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(blank=True, max_length=150, null=True)),
                ('Product_name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expired_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Actual_price', models.FloatField(default=0)),
                ('Final_price', models.FloatField(default=0)),
                ('Total_units', models.PositiveIntegerField(default=0)),
                ('Available_units', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=150, null=True)),
                ('Product_id', models.CharField(blank=True, max_length=150, null=True)),
                ('Product_name', models.CharField(max_length=250)),
                ('Ordered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer_name', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('Ordered_price', models.FloatField(default=0)),
                ('status', models.CharField(default='Received', max_length=50)),
            ],
        ),
    ]
