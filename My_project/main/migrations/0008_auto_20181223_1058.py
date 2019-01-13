# Generated by Django 2.1.4 on 2018-12-23 05:28

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(50000), django.core.validators.MinValueValidator(500)])),
                ('description', models.CharField(default='Balance', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]