# Generated by Django 5.1.2 on 2024-10-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('name', models.CharField()),
                ('email', models.CharField()),
                ('date_of_birth', models.DateField()),
                ('city', models.CharField()),
                ('state', models.CharField()),
                ('country', models.CharField()),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('transaction_type', models.CharField()),
                ('transaction_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('currency', models.CharField()),
            ],
        ),
    ]