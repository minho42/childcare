from django.db import models
from project.models import TimeStampedModel


class Childcare(TimeStampedModel):
    approval_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    suburb = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    postcode = models.CharField(max_length=4)

    rating1 = models.IntegerField(default=0, null=True)
    rating2 = models.IntegerField(default=0, null=True)
    rating3 = models.IntegerField(default=0, null=True)
    rating4 = models.IntegerField(default=0, null=True)
    rating5 = models.IntegerField(default=0, null=True)
    rating6 = models.IntegerField(default=0, null=True)
    rating7 = models.IntegerField(default=0, null=True)
    average_ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0, null=True)
    overall_rating = models.CharField(max_length=100, null=True)
    overall_rating_number = models.IntegerField(default=0, null=True)
    ratings_issued = models.CharField(max_length=20, null=True)

    prev_rating1 = models.IntegerField(default=0, null=True)
    prev_rating2 = models.IntegerField(default=0, null=True)
    prev_rating3 = models.IntegerField(default=0, null=True)
    prev_rating4 = models.IntegerField(default=0, null=True)
    prev_rating5 = models.IntegerField(default=0, null=True)
    prev_rating6 = models.IntegerField(default=0, null=True)
    prev_rating7 = models.IntegerField(default=0, null=True)
    prev_average_ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0, null=True)
    prev_overall_rating = models.CharField(max_length=100, null=True)
    prev_overall_rating_number = models.IntegerField(default=0, null=True)
    prev_ratings_issued = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["approval_number", "name"]
