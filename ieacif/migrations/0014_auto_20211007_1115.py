# Generated by Django 3.1.1 on 2021-10-07 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ieacif', '0013_auto_20211007_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumidores',
            old_name='Renda_Media_Familiar',
            new_name='RendaMediaFamiliar',
        ),
        migrations.RenameField(
            model_name='consumidores',
            old_name='Renda_Media_por_Morador',
            new_name='RendaMediaPorMorador',
        ),
    ]
