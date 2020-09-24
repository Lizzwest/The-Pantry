# Generated by Django 3.1.1 on 2020-09-24 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('grain', 'GRAIN'), ('vegetables', 'VEGETABLES'), ('fruits', 'FRUITS'), ('dairy', 'DAIRY'), ('meat', 'MEAT'), ('misc', 'MISCELLANEOUS')], default='grain', max_length=100)),
                ('itemName', models.CharField(max_length=100)),
                ('weightQuantity', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
