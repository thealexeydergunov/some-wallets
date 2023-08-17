# Generated by Django 4.2.4 on 2023-08-17 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=512)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(max_length=512, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.wallet')),
            ],
        ),
    ]