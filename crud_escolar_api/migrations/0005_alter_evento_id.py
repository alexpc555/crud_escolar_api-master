# Generated by Django 5.0.2 on 2025-05-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_escolar_api', '0004_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
