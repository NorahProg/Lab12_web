# Generated by Django 5.1.6 on 2025-04-27 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0006_company_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookmodule.address')),
            ],
        ),
    ]
