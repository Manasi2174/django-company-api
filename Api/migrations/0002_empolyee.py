# Generated by Django 5.2.4 on 2025-07-29 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Software Developer', 'sd'), ('Project Leader', 'pl')])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.company')),
            ],
        ),
    ]
