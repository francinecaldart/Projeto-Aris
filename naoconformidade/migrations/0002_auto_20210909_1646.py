# Generated by Django 3.1.7 on 2021-09-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naoconformidade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nc',
            name='Descricao',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='nc',
            name='OBS',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='nc',
            name='Prazo',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='nc',
            name='Unidade',
            field=models.CharField(max_length=20, null=True),
        ),
    ]