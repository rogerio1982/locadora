# Generated by Django 2.1.1 on 2018-09-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180916_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locacao',
            name='data_devolucao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='data_locacao',
            field=models.DateField(),
        ),
    ]
