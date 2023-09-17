from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=1000, default='')
    cover = models.CharField(max_length=1000, default='')
    information = models.CharField(max_length=5000, default='')

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
    slogan = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=200, blank=True, null=True)
    pdf = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    starting_quantity = models.CharField(max_length=100, blank=True, null=True)
    starting_price = models.CharField(max_length=100, blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    intro_photo = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    cover_photo = models.JSONField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    perfect_for = models.JSONField(blank=True, null=True)
    ideas = models.JSONField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    artwork = models.JSONField(blank=True, null=True)
    templates = models.JSONField(blank=True, null=True)
    faq = models.JSONField(blank=True, null=True)
    design_services = models.JSONField(blank=True, null=True)
    intro = models.JSONField(blank=True, null=True)
    features = models.JSONField(blank=True, null=True)
    variants = models.JSONField(blank=True, null=True)
    rp = models.CharField(max_length=100, blank=True, null=True)
    dp = models.CharField(max_length=100, blank=True, null=True)
    pricing = models.JSONField(blank=True, null=True)
    price = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
    




