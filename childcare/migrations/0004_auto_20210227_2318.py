# Generated by Django 3.1.7 on 2021-02-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare', '0003_auto_20210227_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childcare',
            name='ratings',
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_average_ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_overall_rating',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_overall_rating_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating4',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating5',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating6',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_rating7',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='prev_ratings_issued',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='childcare',
            name='average_ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]