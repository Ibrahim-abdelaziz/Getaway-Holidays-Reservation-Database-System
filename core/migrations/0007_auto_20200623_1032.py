# Generated by Django 2.2.7 on 2020-06-23 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200623_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='inspection_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='core.Supplier'),
        ),
    ]
