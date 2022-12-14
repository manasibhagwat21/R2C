# Generated by Django 3.2.5 on 2021-10-19 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211015_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('med', models.CharField(default='Crocin', max_length=200, verbose_name='Medicine Name')),
                ('pres', models.FileField(upload_to='Prescriptions')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer')),
            ],
        ),
    ]
