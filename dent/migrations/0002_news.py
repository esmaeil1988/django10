# Generated by Django 4.2.4 on 2023-09-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onvan', models.CharField(max_length=50)),
                ('matn', models.CharField(max_length=800)),
                ('manba', models.CharField(max_length=40)),
                ('aks', models.ImageField(null=True, upload_to='aks')),
            ],
        ),
    ]
