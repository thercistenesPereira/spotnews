from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


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


def validate_title(title):
    if title.count(" ") < 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


class News(models.Model):
    title = models.CharField(
        max_length=200, blank=False, validators=[validate_title]
    )
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to="img/", blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title
