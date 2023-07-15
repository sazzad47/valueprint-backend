from django.contrib import admin
from .models import Category, Product
from django_admin_json_editor import JSONEditorWidget
from django import forms
from .models import Variant, SubVariant, Price, SubVariantOption, Option, Schema, YourModel

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
                                'description': {'type': 'string'}
                            }
                        }
                    }
                }
            }
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
                                'image': {'type': 'string'}
                            }
                        }
                    }
                }
            }
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
                                'answer': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        ),
        required=False
    )

    options = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'description': {'type': 'string'}
                    }
                }
            }
        ),
        required=False
    )

    design_services = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string'},
                        'price': {'type': 'string'},
                        'services': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        }
                    }
                }
            }
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
                        'layout': {'type': 'string'},
                        'allow_customize': {'type': 'boolean'},
                        'value': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'is_default': {'type': 'boolean'},
                                    'is_popular': {'type': 'boolean'},
                                    'photo': {'type': 'string'},
                                    'title': {'type': 'string'},
                                    'description': {'type': 'string'}
                                }
                            }
                        }
                    }
                }
            }
        ),
        required=False
    )

    variants = forms.JSONField(
        widget=JSONEditorWidget(
            schema={
                'type': 'object',
                'properties': {
                    'placeholder': {'type': 'string'},
                    'layout': {'type': 'string'},
                    'value': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'is_default': {'type': 'string'},
                                'is_popular': {'type': 'string'},
                                'photo': {'type': 'string'},
                                'title': {'type': 'string'},
                                'description': {'type': 'string'},
                                'subvariant': {
                                    'type': 'object',
                                    'properties': {
                                        'placeholder': {'type': 'string'},
                                        'layout': {'type': 'string'},
                                        'value': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'is_default': {'type': 'string'},
                                                    'is_popular': {'type': 'string'},
                                                    'photo': {'type': 'string'},
                                                    'title': {'type': 'string'},
                                                    'description': {'type': 'string'},
                                                    'rp': {'type': 'string'},
                                                    'dp': {'type': 'string'},
                                                    'price': {
                                                        'type': 'array',
                                                        'items': {
                                                            'type': 'object',
                                                            'properties': {
                                                                'quantity': {'type': 'string'},
                                                                'price': {'type': 'string'},
                                                                'is_best_seller': {'type': 'boolean'}
                                                            }
                                                        }
                                                    }
                                                }
                                            }
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
                                                    'is_best_seller': {'type': 'boolean'}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
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
                        'is_best_seller': {'type': 'boolean'}
                    }
                }
            }
        ),
        required=False
    )

    class Meta:
        model = Product
        fields = '__all__'

class PriceInline(admin.TabularInline):
    model = Price


class SubVariantOptionInline(admin.TabularInline):
    model = SubVariantOption


class OptionInline(admin.TabularInline):
    model = Option


class ValueInline(admin.TabularInline):
    model = Schema.value.through


class SubVariantInline(admin.TabularInline):
    model = SubVariant


class SchemaAdmin(admin.ModelAdmin):
    inlines = [ValueInline]


class VariantAdmin(admin.ModelAdmin):
    inlines = [SubVariantInline]


class SubVariantAdmin(admin.ModelAdmin):
    inlines = [OptionInline, SubVariantOptionInline]


class YourModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Variant, VariantAdmin)
admin.site.register(SubVariant, SubVariantAdmin)
admin.site.register(Schema, SchemaAdmin)
admin.site.register(YourModel, YourModelAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = OrderAdminForm

admin.site.register(Category)
admin.site.site_header = "Value Printing Pte Ltd Admin"
admin.site.index_title = "Welcome to Value Printing Pte Ltd"
admin.site.site_title = "Value Printing Pte Ltd"
