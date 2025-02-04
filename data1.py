import os
import django
from datetime import datetime

from DjangoProject1 import data

# تنظیمات Django برای شناسایی پروژه
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject1.settings')
django.setup()

from models import Product, SubProductImage


# تابع تبدیل تاریخ به فرمت YYYY-MM-DD
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, '%m/%Y').date().replace(day=1)
    except ValueError:
        return datetime.strptime(date_str, '%Y-%m-%d').date()


# بررسی صحت URL
def is_valid_url(url):
    return not url.startswith('https://www.google.com/url')


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
        expiration_date=convert_date(item['expiration_date'])  # تبدیل تاریخ

    )

    for img in item['subproduct_images']:
        if is_valid_url(img['product_image_src']):
            SubProductImage.objects.create(product=product, product_image_src=img['product_image_src'])

print("محصولات با موفقیت اضافه شدند!")







