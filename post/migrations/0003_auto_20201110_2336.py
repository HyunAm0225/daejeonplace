# Generated by Django 3.1.3 on 2020-11-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20201110_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=50, verbose_name='장소명'),
        ),
    ]
