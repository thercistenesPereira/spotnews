from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    def clean(self):
        if len(self.name) > 200:
            raise ValidationError(
                "O nome não pode ter mais de 200 caracteres."
            )
