import os
import django

from DjangoProject1 import data

# تنظیمات Django برای شناسایی پروژه
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject1.settings')
django.setup()

from models import Product, SubProductImage

for item in data:
    product = Product.objects.create(
        product_name=item['product_name'],
        product_details=item['product_details'],
        main_price=item['main_price'],
        discount=item['discount'],
        final_price=item['final_price'],
        brand=item['brand'],
        brand_image_src=item['brand_image_src'],
        category=item['category'],
        sub_category=item['sub_category'],
        category_image_src=item['category_image_src'],
        size=item['size'],
        production_date=item['production_date'],
        expiration_date=item['production_date'],  # تبدیل تاریخ

    )

    for img in item['subproduct_images']:
        if img['product_image_src']:
            SubProductImage.objects.create(product=product, product_image_src=img['product_image_src'])

print("محصولات با موفقیت اضافه شدند!")







