# Generated by Django 2.0.7 on 2018-08-17 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whichisblank', '0003_auto_20180717_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField()),
                ('correct', models.BooleanField()),
                ('first_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_a', to='whichisblank.Country')),
                ('second_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_b', to='whichisblank.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comp_instance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
