# Generated by Django 5.0.6 on 2024-06-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField()),
                ('Designation', models.CharField(max_length=200)),
                ('Salary', models.IntegerField()),
            ],
        ),
    ]
