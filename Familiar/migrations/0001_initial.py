# Generated by Django 4.1.4 on 2022-12-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('Esta_vivo', models.BooleanField()),
            ],
        ),
    ]
