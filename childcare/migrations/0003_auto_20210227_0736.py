# Generated by Django 3.1.7 on 2021-02-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childcare', '0002_childcare_ratings_issued'),
    ]

    operations = [
        migrations.AddField(
            model_name='childcare',
            name='average_ratings',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='childcare',
            name='overall_rating_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating3',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating4',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating5',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating6',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='rating7',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childcare',
            name='ratings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]