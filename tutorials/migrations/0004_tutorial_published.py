# Generated by Django 2.1.7 on 2019-02-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20190130_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]