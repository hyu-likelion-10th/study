# Generated by Django 2.2.10 on 2021-04-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='num',
        ),
        migrations.AddField(
            model_name='answer',
            name='ans',
            field=models.TextField(default='민정'),
            preserve_default=False,
        ),
    ]