# Generated by Django 5.1 on 2025-06-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='vol',
        ),
        migrations.AddField(
            model_name='produto',
            name='vol_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='emite_nf',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nota',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='un_135',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='un_136',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='un_137',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='un_138',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='vol_cb',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='vol_unif',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
