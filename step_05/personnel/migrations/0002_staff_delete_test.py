# Generated by Django 4.0.2 on 2022-03-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=2)),
                ('edu', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
                ('entry', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
