# Generated by Django 3.1.7 on 2021-02-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcare',
            name='ratings_issued',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
