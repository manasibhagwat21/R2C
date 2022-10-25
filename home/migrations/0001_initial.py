# Generated by Django 3.2.6 on 2021-10-15 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('age', models.CharField(max_length=150, null=True)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(default='Crocin', max_length=200, verbose_name='Medicine Name')),
                ('prescription', models.CharField(default='Y', max_length=500, verbose_name='Prescription')),
                ('Type_of_Sell', models.CharField(max_length=500, null=True, verbose_name='Type of Sell')),
                ('manufacturer', models.CharField(default='Cipla', max_length=500, verbose_name='Manufacturer')),
                ('salt', models.CharField(max_length=500, null=True, verbose_name='Salt')),
                ('mrp', models.CharField(default='50', max_length=500, verbose_name='MRP')),
                ('uses', models.CharField(max_length=500, null=True, verbose_name='Uses')),
                ('Side_Effects', models.CharField(max_length=500, null=True, verbose_name='Side Effects')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
                ('medicines', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.medicine')),
            ],
        ),
    ]