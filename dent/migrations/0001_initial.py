# Generated by Django 4.2.4 on 2023-09-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('onvan', models.CharField(max_length=30)),
                ('matn', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=20)),
                ('famil', models.CharField(max_length=20)),
                ('takhasos', models.CharField(max_length=80)),
                ('adress', models.CharField(max_length=40)),
                ('img', models.ImageField(null=True, upload_to='aks')),
            ],
        ),
    ]