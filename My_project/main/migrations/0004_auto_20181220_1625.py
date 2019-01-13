# Generated by Django 2.1.4 on 2018-12-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181220_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('C', 'Current_Account'), ('S', 'Saving_Account'), ('F', 'Fixed_Deposit'), ('R', 'Recurring_Deposit')], max_length=4),
        ),
    ]