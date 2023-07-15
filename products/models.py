from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    cover = models.CharField(max_length=200, blank=True, null=True)
    information = models.CharField(max_length=3000, blank=True, null=True)
    artwork = models.JSONField(blank=True, null=True)
    templates = models.JSONField(blank=True, null=True)
    faq = models.JSONField(blank=True, null=True)
    design_services = models.JSONField(blank=True, null=True)
    features = models.JSONField(blank=True, null=True)
    variants = models.JSONField(blank=True, null=True)
    rp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Variant(models.Model):
    placeholder = models.CharField(max_length=255)


class SubVariant(models.Model):
    placeholder = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


class Price(models.Model):
    quantity = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    is_best_seller = models.BooleanField()


class SubVariantOption(models.Model):
    is_default = models.CharField(max_length=255)
    is_popular = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rp = models.CharField(max_length=255)
    dp = models.CharField(max_length=255)
    price = models.ManyToManyField(Price)
    subvariant = models.ForeignKey(SubVariant, on_delete=models.CASCADE)


class Option(models.Model):
    is_default = models.CharField(max_length=255)
    is_popular = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    subvariant = models.ForeignKey(SubVariant, on_delete=models.CASCADE)
    rp = models.CharField(max_length=255)
    dp = models.CharField(max_length=255)
    price = models.ManyToManyField(Price)


class Schema(models.Model):
    placeholder = models.CharField(max_length=255)
    value = models.ManyToManyField(Option)


class YourModel(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)





