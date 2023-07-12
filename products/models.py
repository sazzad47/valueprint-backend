from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
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




