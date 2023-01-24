# Generated by Django 4.1.1 on 2023-01-24 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=50)),
                ('compinst', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('requestdesc', models.TextField(null=True)),
                ('document', models.FileField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=10, null=True)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('institute', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=50)),
                ('areaofinterest', models.CharField(max_length=50)),
                ('hours', models.CharField(max_length=10)),
                ('resume', models.FileField(upload_to='media')),
            ],
        ),
    ]