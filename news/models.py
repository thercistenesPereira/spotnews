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


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def clean(self):
        if len(self.name) > 200:
            raise ValidationError(
                "O nome não pode ter mais de 200 caracteres."
            )
        if len(self.email) > 200:
            raise ValidationError(
                "O email não pode ter mais de 200 caracteres."
            )
        if len(self.password) > 200:
            raise ValidationError(
                "A senha não pode ter mais de 200 caracteres."
            )
        if len(self.role) > 200:
            raise ValidationError(
                "O papel não pode ter mais de 200 caracteres."
            )
