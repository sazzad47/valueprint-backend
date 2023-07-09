from django.contrib import admin
from .models import Category, Product
from django_admin_json_editor import JSONEditorWidget
from django import forms

class OrderAdminForm(forms.ModelForm):
    artwork = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'object',
                'properties': {
                    'instruction': {'type': 'string'},
                    'content': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {'type': 'string'},
                                'description': {'type': 'string'},
                            },
                        },
                    },
                },
            },
        ),
        required=False
    )

    templates = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'object',
                'properties': {
                    'instruction': {'type': 'string'},
                    'content': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'format': {'type': 'string'},
                                'pdf': {'type': 'string'},
                                'image': {'type': 'string'},
                            },
                        },
                    },
                },
            },
        ),
        required=False
    )

    faq = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'object',
                'properties': {
                    'instruction': {'type': 'string'},
                    'content': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'question': {'type': 'string'},
                                'answer': {'type': 'string'},
                            },
                        },
                    },
                },
            },
        ),
        required=False
    )


    features = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'placeholder': {'type': 'string'},
                        'value': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                            },
                        },
                    },
                },
            },
        ),
        required=False
    )

    variants = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'subvariant': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'rp': {'type': 'string'},
                                    'dp': {'type': 'string'},
                                    'price': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'properties': {
                                                'quantity': {'type': 'string'},
                                                'price': {'type': 'string'},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'rp': {'type': 'string'},
                        'dp': {'type': 'string'},
                        'price': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'quantity': {'type': 'string'},
                                    'price': {'type': 'string'},
                                },
                            },
                        },
                    },
                },
            },
        ),
        required=False
    )

    price = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'quantity': {'type': 'string'},
                        'price': {'type': 'string'},
                    },
                },
            },
        ),
        required=False
    )

    class Meta:
        model = Product
        fields = '__all__'



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = OrderAdminForm

admin.site.register(Category)
