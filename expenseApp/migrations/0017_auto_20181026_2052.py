# Generated by Django 2.0.6 on 2018-10-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0016_auto_20181026_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='checking',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='deposit',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='expense',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='savings',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]