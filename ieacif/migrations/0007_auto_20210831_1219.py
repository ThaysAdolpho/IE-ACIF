# Generated by Django 3.1.1 on 2021-08-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieacif', '0006_auto_20210831_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='Atividade_Econômica_CNAE',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='CNPJ',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='Endereço',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='Porte',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='Razão_Social',
            field=models.CharField(max_length=10000),
        ),
    ]