# Generated by Django 4.1.2 on 2022-10-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisioterapias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.DateTimeField(),
        ),
    ]
