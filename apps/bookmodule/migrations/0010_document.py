# Generated by Django 5.1.6 on 2025-04-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0009_remove_address2_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
