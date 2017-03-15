from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators

RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class Pub(models. Model):
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)

    overall = models.CharField(max_length=16, choices=RATING)
    design = models.FloatField(blank=True, null=True, validators=(validators.MinValueValidator(0.0),
                                                                validators.MaxValueValidator(1.0)))
    design_description = models.TextField(blank=True, null=True)
    atmosphere = models.FloatField(blank=True, null=True, validators=(validators.MinValueValidator(0.0),
                                                                    validators.MaxValueValidator(1.0)))
    atmosphere_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.city


    class Meta:
        verbose_name = _('pub')
        verbose_name_plural = _('pubs')
