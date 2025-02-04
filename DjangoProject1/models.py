from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_details = models.TextField()
    main_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    brand = models.CharField(max_length=255)
    brand_image_src = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    production_date = models.DateField()
    expiration_date = models.DateField()
    category_image_src = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.final_price = self.main_price - (self.main_price * (self.discount / 100))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class SubProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='subproduct_images', on_delete=models.CASCADE)
    product_image_src = models.URLField()

    def __str__(self):
        return f"Image for {self.product.product_name}"

