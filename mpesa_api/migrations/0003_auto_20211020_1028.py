# Generated by Django 3.2.8 on 2021-10-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0002_lnmpesaonline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpesapayment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='organization_balance',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='type',
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='Balance',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='CheckoutRequestID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='MerchantRequestID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='MpesaReceiptNumber',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='PhoneNumber',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='ResultCode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='ResultDesc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='lnmpesaonline',
            name='TransactionDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]