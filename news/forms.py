from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "name",
                    "maxlength": 200,
                    "required": True,
                }
            )
        }
