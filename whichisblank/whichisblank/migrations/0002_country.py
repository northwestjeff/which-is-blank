# Generated by Django 2.0.7 on 2018-07-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whichisblank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
                ('capital_city', models.CharField(max_length=200)),
            ],
        ),
    ]
