# Generated by Django 2.0.6 on 2018-10-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApp', '0004_expensesmodel_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesmodel',
            name='account_name',
            field=models.CharField(blank=True, default='NO MODEL', max_length=200, null=True),
        ),
    ]