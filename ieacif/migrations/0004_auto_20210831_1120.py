# Generated by Django 3.1.1 on 2021-08-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieacif', '0003_consumidores_consumo_empresas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumidores',
            name='Bairros',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Hab_Total',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Max',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Moradores',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Média',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Mín',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Renda_Média_Familiar',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='consumidores',
            name='Renda_Média_por_Morador',
            field=models.CharField(max_length=1000),
        ),
    ]
