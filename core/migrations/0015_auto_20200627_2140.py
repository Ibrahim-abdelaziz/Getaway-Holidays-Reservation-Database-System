# Generated by Django 2.2.7 on 2020-06-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200625_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='agent_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='agent_signature',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='client_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='client_signature',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
