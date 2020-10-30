from django.db import models
from django.contrib.auth.models import User

SHARP = (
    ('H', 'Hone'),
    ('S', 'Sharpen'),
    ('G', 'Grind')
)

# Create your models here.

class Prep(models.Model):
    product = models.CharField(max_length=100)
    specs = models.CharField(max_length=50)

    def __str__(self):
        return self.product


class Cutlery(models.Model):
    maker = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    use = models.CharField(max_length=100) 
    steel = models.CharField(max_length=100)
    price = models.IntegerField()
    prep = models.ManyToManyField(Prep)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.maker

class Sharpen(models.Model):
    date = models.DateField('sharpen date')
    sharp = models.CharField(
        max_length=1,
        choices=SHARP,
        default=SHARP[0][0]
    )
    cutlery = models.ForeignKey(Cutlery, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_sharp_display()} on {self.date}'


