# Generated by Django 3.1.7 on 2021-09-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naoconformidade', '0002_auto_20210909_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='nc',
            name='Situacao',
            field=models.CharField(choices=[('Pendete', 'Pendete')], max_length=20, null=True),
        ),
    ]
