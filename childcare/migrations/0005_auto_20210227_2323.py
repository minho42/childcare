# Generated by Django 3.1.7 on 2021-02-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare', '0004_auto_20210227_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childcare',
            name='average_ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='overall_rating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='overall_rating_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_average_ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_overall_rating',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_overall_rating_number',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating6',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_rating7',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='prev_ratings_issued',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating5',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating6',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='rating7',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='childcare',
            name='ratings_issued',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
