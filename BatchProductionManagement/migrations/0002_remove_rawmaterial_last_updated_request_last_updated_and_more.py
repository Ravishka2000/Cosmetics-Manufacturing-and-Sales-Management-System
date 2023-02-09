# Generated by Django 4.1.2 on 2022-11-02 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FormulationAndLabManagement', '0003_alter_formulation_formulation_qty_and_more'),
        ('BatchProductionManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmaterial',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='request',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='schedule_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='BatchProductionManagement.scheduleproduction'),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_requested',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduleproduction',
            name='product_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='FormulationAndLabManagement.products'),
        ),
    ]
