# Generated by Django 3.2.4 on 2021-06-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0002_auto_20210604_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40, verbose_name='姓名'),
        ),
    ]
