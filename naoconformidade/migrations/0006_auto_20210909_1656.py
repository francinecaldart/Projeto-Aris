# Generated by Django 3.1.7 on 2021-09-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naoconformidade', '0005_auto_20210909_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nc',
            name='Situacao',
            field=models.CharField(choices=[('A', 'Atendida'), ('P', 'Pendente')], max_length=1, null=True),
        ),
    ]
