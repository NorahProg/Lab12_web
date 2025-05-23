# Generated by Django 5.1.6 on 2025-04-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmodule', '0007_student2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('addresses', models.ManyToManyField(to='bookmodule.address2')),
            ],
        ),
    ]
