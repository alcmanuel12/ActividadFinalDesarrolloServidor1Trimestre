from django.db import models

class Party(models.Model):
    name = models.CharField(max_length=100)
    attendants = models.IntegerField()

    def __str__(self):
        return self.name

class Animatronic(models.Model):

    ANIMAL_CHOICES = [
        ('BE', 'Bear'),
        ('CH', 'Chicken'),
        ('BU', 'Bunny'),
        ('FO', 'Fox'),
    ]

    name = models.CharField(
        max_length=50,
        verbose_name="Name"
    )

    animal = models.CharField(
        max_length=2,
        choices=ANIMAL_CHOICES,
        verbose_name="Animal type"
    )


    build_date = models.DateField(
        verbose_name="Build date"
    )


    decommissioned = models.BooleanField(
        default=False,
        verbose_name="Decommissioned"
    )


    parties = models.ManyToManyField(
        Party,
        blank=True,
        verbose_name="Parties"
    )

    def __str__(self):
        return self.name