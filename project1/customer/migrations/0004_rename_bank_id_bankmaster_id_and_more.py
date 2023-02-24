# Generated by Django 4.1.7 on 2023-02-23 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_bankmaster_customerbankaccount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankmaster',
            old_name='bank_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='customerbankaccount',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to='customer.bankmaster'),
        ),
        migrations.AlterField(
            model_name='customerbankaccount',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_bank_accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]