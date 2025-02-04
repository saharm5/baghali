# data.py
from django.http import JsonResponse


def get_data(request):
    data = [
        {
            "id": 1,
            "product_name": "چیپس نمکی",
            "product_details": "بسته ۱۰۰ گرمی چیپس طعم نمک",
            "main_price": 20000,
            "final_price": 10,
            "finalPrice": 18000,
            "brand": "چی توز",
            "brand_image_src": "https://logoyab.com/wp-content/uploads/2024/06/Cheetoz-Logo-450x450.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/e01173ed-b86a-4bfa-8384-6b24dec727b7.jpg"},
                {
                    "productImageSrc": "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftorob.com%2Fp%2F35f3b00c-793d-4aba-849c-3a2b5eb91954%2F%25DA%2586%25DB%258C%25D9%25BE%25D8%25B3-%25D8%25B3%25D8%25A7%25D8%25AF%25D9%2587-%25D9%2586%25D9%2585%25DA%25A9%25DB%258C-%25DA%2586%25DB%258C-%25D8%25AA%25D9%2588%25D8%25B2-140-%25DA%25AF%25D8%25B1%25D9%2585%25DB%258C%2F&psig=AOvVaw1FEP_FSHwwmbxewE1keNCL&ust=1737976051848000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODy8Mmfk4sDFQAAAAAdAAAAABAJ"},
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/e01173ed-b86a-4bfa-8384-6b24dec727b7.jpg"},
                {
                    "productImageSrc": "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftorob.com%2Fp%2F35f3b00c-793d-4aba-849c-3a2b5eb91954%2F%25DA%2586%25DB%258C%25D9%25BE%25D8%25B3-%25D8%25B3%25D8%25A7%25D8%25AF%25D9%2587-%25D9%2586%25D9%2585%25DA%25A9%25DB%258C-%25DA%2586%25DB%258C-%25D8%25AA%25D9%2588%25D8%25B2-140-%25DA%25AF%25D8%25B1%25D9%2585%25DB%258C%2F&psig=AOvVaw1FEP_FSHwwmbxewE1keNCL&ust=1737976051848000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCODy8Mmfk4sDFQAAAAAdAAAAABAJ"},
            ],
            "category": "تنقلات",
            "sub_category": "چیپس و پفک",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 2,
            "product_name": "پفک نمکی",
            "product_details": "بسته ۵۰ گرمی پفک نمکی",
            "main_price": 5000,
            "final_price": 5,
            "finalPrice": 4750,
            "brand": "چی توز",
            "brand_image_src": "https://logoyab.com/wp-content/uploads/2024/06/Cheetoz-Logo-450x450.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/12575.png"},
                {
                    "productImageSrc": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fginaco.de%2Fprodukt%2Fchitooz-gold-gross%2F&psig=AOvVaw3kBRGV99A_uGUH-G-ocf_K&ust=1737976772627000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCOjQqpqik4sDFQAAAAAdAAAAABAE"},
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/12575.png"},
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/12575.png"},
                {
                    "productImageSrc": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fginaco.de%2Fprodukt%2Fchitooz-gold-gross%2F&psig=AOvVaw3kBRGV99A_uGUH-G-ocf_K&ust=1737976772627000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCOjQqpqik4sDFQAAAAAdAAAAABAE"}
            ],
            "category": "تنقلات",
            "sub_category": "چیپس و پفک",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 3,
            "product_name": "شکلات تلخ",
            "product_details": "شکلات تلخ ۹۰ درصد، بسته ۱۵۰ گرمی",
            "main_price": 150000,
            "final_price": 0,
            "finalPrice": 150000,
            "brand": "آیدین",
            "brand_image_src": "https://example.com/brands/chocolatco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/119425007.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://zerocalories.ir/wp-content/uploads/2024/06/%D8%B4%DA%A9%D9%84%D8%A7%D8%AA-%D8%AA%D9%84%D8%AE-90-%D8%AF%D8%B1%D8%B5%D8%AF-600x600.jpg"},
                {
                    "productImageSrc": "https://zerocalories.ir/wp-content/uploads/2024/06/%D8%B4%DA%A9%D9%84%D8%A7%D8%AA-%D8%AA%D9%84%D8%AE-90-%D8%AF%D8%B1%D8%B5%D8%AF-600x600.jpg"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/119425007.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://zerocalories.ir/wp-content/uploads/2024/06/%D8%B4%DA%A9%D9%84%D8%A7%D8%AA-%D8%AA%D9%84%D8%AE-90-%D8%AF%D8%B1%D8%B5%D8%AF-600x600.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "شکلات و آبنبات",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 4,
            "product_name": "پاستیل رنگی",
            "product_details": "بسته ۲۰۰ گرمی پاستیل رنگی",
            "main_price": 8000,
            "final_price": 5,
            "finalPrice": 7600,
            "brand": "شیبا",
            "brand_image_src": "https://logoyab.com/wp-content/uploads/2024/06/Shiba-Logo-1030x1030.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://www.martestan.com/upload/thumb1/product/1682520590-%D8%B4%DB%8C%D8%A8%D8%A7.jpg"},
                {
                    "productImageSrc": "https://measomarket.com/uploads/products_images/156876-296x362.webp"},
                {
                    "productImageSrc": "https://www.martestan.com/upload/thumb1/product/1682520590-%D8%B4%DB%8C%D8%A8%D8%A7.jpg"},
                {
                    "productImageSrc": "https://www.martestan.com/upload/thumb1/product/1682520590-%D8%B4%DB%8C%D8%A8%D8%A7.jpg"},
                {
                    "productImageSrc": "https://measomarket.com/uploads/products_images/156876-296x362.webp"}
            ],
            "category": "تنقلات",
            "sub_category": "پاستیل و آدامس",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 5,
            "product_name": "کیک شکلاتی",
            "product_details": "کیک شکلاتی ۴۰۰ گرمی",
            "main_price": 10000,
            "final_price": 10,
            "finalPrice": 9000,
            "brand": "درنا",
            "brand_image_src": "https://tiktarh.com/wp-content/uploads/2024/07/RLg1001001www.tiktarh.com_.jpg",
            "SubproductImages": [
                {
                    "productImageSrc": "https://shp.aradbranding.com/images/2024/07/1721912419_8890d33f31200e926ee5fdd074f5691112ae8720_1635145909.jpg"},
                {
                    "productImageSrc": "https://img.beroozmart.com/unsafe/fit-in/450x450/files/shop/product/403234fc3e58444f85355ec3f3e0058e.jpg"},
                {
                    "productImageSrc": "https://image.torob.com/base/images/uZ/Y6/uZY6HMq-aFkVeW9C.jpg_/280x280.jpg"},
                {
                    "productImageSrc": "https://shp.aradbranding.com/images/2024/07/b3e8a05d2f0e4f868e9f0865e02ebfd2.jpg"},
            ],
            "category": "تنقلات",
            "sub_category": "کیک و کلوچه",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 6,
            "product_name": "آبنبات نعنا",
            "product_details": "آبنبات نعنا ۲۹ گرمی",
            "main_price": 4000,
            "final_price": 0,
            "finalPrice": 4000,
            "brand": "منتوس",
            "brand_image_src": "https://banner2.cleanpng.com/20180713/evf/aaww3wif1.webp",
            "SubproductImages": [
                {
                    "productImageSrc": "https://www.halachi.net/wp-content/uploads/2021/12/mentos.mint_.37.5gr.packof20.sepehrmall.com_.jpg"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/b1bb914042c274f056a98f772df03f332641b520_1620481828.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://www.halachi.net/wp-content/uploads/2021/12/126949-01_mint-mentos-candy-rolls-15-piece-box.jpg"},
                {
                    "productImageSrc": "https://tanagholat.com/5719-large_default/%D8%A2%D8%AF%D8%A7%D9%85%D8%B3-%D9%85%D9%86%D8%AA%D9%88%D8%B3-%D9%85%D8%AF%D9%84-%D9%84%D9%88%D9%84%D9%87-%D8%A7%DB%8C-%D8%A8%D8%A7-%D8%B7%D8%B9%D9%85-%D9%86%D8%B9%D9%86%D8%A7.jpg"},
            ],
            "category": "تنقلات",
            "sub_category": "شکلات و آبنبات",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 7,
            "product_name": "لواشک میوه‌ای",
            "product_details": "لواشک میوه‌ای ۱۵۰ گرمی",
            "main_price": 5000,
            "final_price": 5,
            "finalPrice": 4750,
            "brand": "نازلی",
            "brand_image_src": "https://example.com/brands/fruitco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWUBlOM3bnSQYDH0UPotPIa5ge2BFdnHibRw&s"},
                {
                    "productImageSrc": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyRA0mzzSCYNRrkBrE6Z4dpVCgL78ZscEueWTB1OBU20o0xCloJpbsGRcfSUK76Ew0_dA&usqp=CAU"},
                {
                    "productImageSrc": "https://hyperweonline.ir/Opitures/267323074023655.jpg"},
                {
                    "productImageSrc": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHU-ZAZy9Ltu0NYH_tN-4HIlBhrT9YOPIw3ASADfJ3L4a_GDWbi_L-tLn3_HkA3hIi2rI&usqp=CAU"},
            ],
            "category": "تنقلات",
            "sub_category": "لواشک و آلوچه",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 8,
            "product_name": "تخمه آفتابگردان",
            "product_details": "تخمه آفتابگردان ۴۰ گرمی",
            "main_price": 3000,
            "final_price": 0,
            "finalPrice": 3000,
            "brand": "مزمز",
            "brand_image_src": "https://logoyab.com/wp-content/uploads/2023/12/%D9%84%D9%88%DA%AF%D9%88-%D9%85%D8%B2%D9%85%D8%B2-450x450.png",
            "SubproductImages": [
                {"productImageSrc": "https://shahrvand.ir/upload/product/1473480682.jpg"},
                {
                    "productImageSrc": "https://api.snapp.market/media/cache/product_variation_transparent_image/33853-20000.png"},
                {"productImageSrc": "https://jamkharid.ir/uploads/products/2ceaf6.jpg?m=crop&w=500&h=500&q=high"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/4085513.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/4085515.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"}
            ],
            "category": "تنقلات",
            "sub_category": "تخمه و مغزیجات طعم دار",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 9,
            "product_name": "مینی تست مخصوص",
            "product_details": "مینی تست مخصوص پرونان نان آوران مقدار 400 گرم",
            "main_price": 40000,
            "final_price": 0,
            "finalPrice": 40000,
            "brand": "نان آوران",
            "brand_image_src": "https://example.com/brands/breadco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/43f283f01eb2da7b5c64b028d0b7658d352d71bb_1730896619.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/119225367.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/d899e0714117e040ffa6f09c50cdb4bde256af4f_1615636460.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/1c15f61984bc8595d389ca4eede8545b96dea70f_1633179138.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "خواربار",
            "sub_category": "نان",
            "category_image_src": "https://example.com/categories/groceries.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 10,
            "product_name": "شکر سفید",
            "product_details": "شکر سفید الماس دانه - 1 کیلوگرم",
            "main_price": 40500,
            "final_price": 0,
            "finalPrice": 40500,
            "brand": "الماس دانه",
            "brand_image_src": "https://example.com/brands/sugarco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/dba25b58eb5b78d2cbf41d5befd49e5f5f64b5e4_1730022468.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/ddef5cca3be676317afd07367c48b4cbbfbcb111_1719947137.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/12881b5e1643b33a33570e0e21476a205cd03bf0_1723032327.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
            ],
            "category": "خواربار",
            "sub_category": "شکر قند و نبات",
            "category_image_src": "https://example.com/categories/groceries.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 11,
            "product_name": "روغن مایع",
            "product_details": "روغن آفتابگردان حاوی توکوفرول غنچه پلاس - 1500 میلی لیتر",
            "main_price": 95000,
            "final_price": 10,
            "finalPrice": 85500,
            "brand": "غنچه",
            "brand_image_src": "https://example.com/brands/oilco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/6ea8d1688bd9dda01dc7f5716bb7c84e9d9c3a0d_1652694148.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/809aadaccdf35d0730b76236ebc66561649050f0_1668247019.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
            ],
            "category": "خواربار",
            "sub_category": "روغن و چربی",
            "category_image_src": "https://example.com/categories/groceries.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 12,
            "product_name": "برنج ایرانی",
            "product_details": "برنج صدری هاشمی ۵ کیلویی",
            "main_price": 60000,
            "final_price": 5,
            "finalPrice": 57000,
            "brand": "آقاجانیان",
            "brand_image_src": "https://example.com/brands/riceco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773600.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773596.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773607.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "خواربار",
            "sub_category": "برنج و حبوبات",
            "category_image_src": "https://example.com/categories/groceries.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 13,
            "product_name": "ماکارونی",
            "product_details": "ماکارونی فرمی پنه کوچک مانا ۵۰۰ گرمی",
            "main_price": 387390,
            "final_price": 25,
            "finalPrice": 292200,
            "brand": "مانا",
            "brand_image_src": "https://logoyab.com/wp-content/uploads/2024/06/Mana-Logo-450x450.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/0a7a3c51ece41abeb5251843ce8ac5eb09f792bc_1716639637.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/931030949518a53daad7029f5a7af5754e0a11a3_1716639640.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/8366dba81ba05c1612e894f66fb4bf7568655ba3_1716639642.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "خواربار",
            "sub_category": "ماکارونی و پاستا",
            "category_image_src": "https://example.com/categories/groceries.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 14,
            "product_name": "پنیر پیتزا",
            "product_details": "پنیر پیتزا مطهر  1 کیلوگرم",
            "main_price": 6000,
            "final_price": 10,
            "finalPrice": 5400,
            "brand": "مطهر",
            "brand_image_src": "https://example.com/brands/cheeseco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/644e94c638aaffb8900ec822ad7994884e043177_1605073012.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/34fc75358456757aa1a43c64b780eba6c8220836_1652882696.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/f049adf38d47e21ef12d31a0f774acdff314f3a4_1605073016.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/0cf161bc503f0a1270008732cead1bdd1493164a_1605073017.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "محصولات لبنی",
            "sub_category": "پنیر",
            "category_image_src": "https://example.com/categories/dairy.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 15,
            "product_name": "شیر کم چرب",
            "product_details": "شیر کم چرب ۱ لیتر",
            "main_price": 9000,
            "final_price": 0,
            "finalPrice": 9000,
            "brand": "شیرکو",
            "brand_image_src": "https://example.com/brands/milco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/437288.png"},
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/437288.png"},
                {
                    "productImageSrc": "https://asset.okala.com/unsigned/rs:fill/size:0:0/plain/s3://cdn//product/437288.png"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات لبنی",
            "sub_category": "شیر",
            "category_image_src": "https://example.com/categories/dairy.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 16,
            "product_name": "خامه پاستوریزه",
            "product_details": "خامه پاستوریزه ۲۰۰ گرمی",
            "main_price": 80000,
            "final_price": 5,
            "finalPrice": 76000,
            "brand": "خامه‌کو",
            "brand_image_src": "https://example.com/brands/creamco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات لبنی",
            "sub_category": "خامه",
            "category_image_src": "https://example.com/categories/dairy.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 17,
            "product_name": "تخم مرغ",
            "product_details": "تخم مرغ ۱۲ عددی",
            "main_price": 8000,
            "final_price": 5,
            "finalPrice": 7600,
            "brand": "تخم‌مرغ‌کو",
            "brand_image_src": "https://example.com/brands/eggco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "sub_category": "تخم مرغ",
            "category_image_src": "https://example.com/categories/protein.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 18,
            "product_name": "گوشت مرغ",
            "product_details": "گوشت مرغ ۱ کیلوگرم",
            "main_price": 300000,
            "final_price": 0,
            "finalPrice": 300000,
            "brand": "مرغ‌کو",
            "brand_image_src": "https://example.com/brands/chickenco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "sub_category": "گوشت و مرغ",
            "category_image_src": "https://example.com/categories/protein.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 19,
            "product_name": "ماهی قزل‌آلا",
            "product_details": "ماهی قزل‌آلا ۵۰۰ گرمی",
            "main_price": 400000,
            "final_price": 5,
            "finalPrice": 380000,
            "brand": "ماهی‌کو",
            "brand_image_src": "https://example.com/brands/fishco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "sub_category": "ماهی و میگو",
            "category_image_src": "https://example.com/categories/protein.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 20,
            "product_name": "پنیر فتا",
            "product_details": "پنیر فتا ۲۵۰ گرمی",
            "main_price": 12000,
            "final_price": 0,
            "finalPrice": 12000,
            "brand": "پنیر‌کو",
            "brand_image_src": "https://example.com/brands/cheeseco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات لبنی",
            "sub_category": "پنیر",
            "category_image_src": "https://example.com/categories/dairy.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        }, {
            "id": 21,
            "product_name": "ماکارونی پنیری",
            "product_details": "ماکارونی پنیری ۴۰۰ گرمی",
            "main_price": 8000,
            "final_price": 0,
            "finalPrice": 8000,
            "brand": "ماکارونی‌پنیری‌کو",
            "brand_image_src": "https://example.com/brands/pastapastico.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "غذای آماده",
            "sub_category": "ماکارونی",
            "category_image_src": "https://example.com/categories/readyfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 22,
            "product_name": "پفک رنگی",
            "product_details": "پفک رنگی ۵۰ گرمی",
            "main_price": 6000,
            "final_price": 5,
            "finalPrice": 5700,
            "brand": "پفکو",
            "brand_image_src": "https://example.com/brands/pofco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "پفک و چیپس",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 23,
            "product_name": "آبمیوه طبیعی",
            "product_details": "آبمیوه طبیعی ۱ لیتر",
            "main_price": 10000,
            "final_price": 10,
            "finalPrice": 9000,
            "brand": "آبمیوه‌کو",
            "brand_image_src": "https://example.com/brands/juiceco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "آبمیوه و نوشیدنی‌های طبیعی",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 24,
            "product_name": "مربای توت فرنگی",
            "product_details": "مربای توت فرنگی ۴۰۰ گرمی",
            "main_price": 6000,
            "final_price": 5,
            "finalPrice": 5700,
            "brand": "مرباکو",
            "brand_image_src": "https://example.com/brands/jamco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "مربا و عسل",
            "sub_category": "مربا",
            "category_image_src": "https://example.com/categories/jam.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 25,
            "product_name": "عسل طبیعی",
            "product_details": "عسل طبیعی ۳۰۰ گرمی",
            "main_price": 15000,
            "final_price": 0,
            "finalPrice": 15000,
            "brand": "عسل‌کو",
            "brand_image_src": "https://example.com/brands/honeyco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "مربا و عسل",
            "sub_category": "عسل",
            "category_image_src": "https://example.com/categories/jam.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 26,
            "product_name": "پودر قهوه",
            "product_details": "پودر قهوه ۲۰۰ گرمی",
            "main_price": 12000,
            "final_price": 5,
            "finalPrice": 11400,
            "brand": "قهوه‌کو",
            "brand_image_src": "https://example.com/brands/coffeeco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "قهوه و نسکافه",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 27,
            "product_name": "چای سیاه",
            "product_details": "چای سیاه ۵۰۰ گرمی",
            "main_price": 10000,
            "final_price": 5,
            "finalPrice": 9500,
            "brand": "چای‌کو",
            "brand_image_src": "https://example.com/brands/teaco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "چای",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 28,
            "product_name": "شکلات شیرین",
            "product_details": "شکلات شیرین ۲۵۰ گرمی",
            "main_price": 12000,
            "final_price": 10,
            "finalPrice": 10800,
            "brand": "شکلات‌کو",
            "brand_image_src": "https://example.com/brands/chocolatco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "شکلات",
            "sub_category": "شکلات‌های شیرین",
            "category_image_src": "https://example.com/categories/chocolate.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 29,
            "product_name": "شکلات تلخ",
            "product_details": "شکلات تلخ ۷۰ درصد ۲۵۰ گرمی",
            "main_price": 15000,
            "final_price": 5,
            "finalPrice": 14250,
            "brand": "شکلات‌تلخ‌کو",
            "brand_image_src": "https://example.com/brands/darkchocolatco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "شکلات",
            "sub_category": "شکلات‌های تلخ",
            "category_image_src": "https://example.com/categories/chocolate.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 30,
            "product_name": "بیسکویت کرمدار",
            "product_details": "بیسکویت کرمدار ۴۰۰ گرمی",
            "main_price": 8000,
            "final_price": 0,
            "finalPrice": 8000,
            "brand": "بیسکویت‌کو",
            "brand_image_src": "https://example.com/brands/biscuitco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "بیسکویت",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 31,
            "product_name": "پاستیل خوشمزه",
            "product_details": "پاستیل خوشمزه ۲۰۰ گرمی",
            "main_price": 4000,
            "final_price": 5,
            "finalPrice": 3800,
            "brand": "پاستیل‌کو",
            "brand_image_src": "https://example.com/brands/gummyco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "پاستیل",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 32,
            "product_name": "آب معدنی",
            "product_details": "آب معدنی ۱٫۵ لیتری",
            "main_price": 3000,
            "final_price": 0,
            "finalPrice": 3000,
            "brand": "آب‌معدنی‌کو",
            "brand_image_src": "https://example.com/brands/mineralco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "آب",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        }, {
            "id": 33,
            "product_name": "دمنوش گیاهی",
            "product_details": "دمنوش گیاهی ۲۰ عددی",
            "main_price": 6000,
            "final_price": 0,
            "finalPrice": 6000,
            "brand": "دمنوش‌کو",
            "brand_image_src": "https://example.com/brands/herbaltea.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "دمنوش",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 34,
            "product_name": "آبنبات شکری",
            "product_details": "آبنبات شکری ۲۰۰ گرمی",
            "main_price": 5000,
            "final_price": 10,
            "finalPrice": 4500,
            "brand": "آبنبات‌کو",
            "brand_image_src": "https://example.com/brands/candyco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "آبنبات و آبنبات شکری",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 35,
            "product_name": "کنسرو ذرت",
            "product_details": "کنسرو ذرت ۴۰۰ گرمی",
            "main_price": 7000,
            "final_price": 0,
            "finalPrice": 7000,
            "brand": "ذرت‌کو",
            "brand_image_src": "https://example.com/brands/cornco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "کنسرو و غذای آماده",
            "sub_category": "کنسرو سبزیجات",
            "category_image_src": "https://example.com/categories/cannedfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 36,
            "product_name": "کنسرو ماهی تن",
            "product_details": "کنسرو ماهی تن ۱۸۰ گرمی",
            "main_price": 10000,
            "final_price": 5,
            "finalPrice": 9500,
            "brand": "ماهی‌کو",
            "brand_image_src": "https://example.com/brands/fishco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "کنسرو و غذای آماده",
            "sub_category": "کنسرو ماهی",
            "category_image_src": "https://example.com/categories/cannedfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 37,
            "product_name": "پودر سوخاری",
            "product_details": "پودر سوخاری ۳۰۰ گرمی",
            "main_price": 5000,
            "final_price": 10,
            "finalPrice": 4500,
            "brand": "پودر سوخاری‌کو",
            "brand_image_src": "https://example.com/brands/fryingco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "چاشنی و ادویه",
            "sub_category": "پودر سوخاری",
            "category_image_src": "https://example.com/categories/spices.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 38,
            "product_name": "شکلات شکری",
            "product_details": "شکلات شکری ۳۰۰ گرمی",
            "main_price": 11000,
            "final_price": 0,
            "finalPrice": 11000,
            "brand": "شکلات‌شکری‌کو",
            "brand_image_src": "https://example.com/brands/sugarchocolateco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "شکلات",
            "sub_category": "شکلات‌های شیرین",
            "category_image_src": "https://example.com/categories/chocolate.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 39,
            "product_name": "پفک نمکی",
            "product_details": "پفک نمکی ۷۰ گرمی",
            "main_price": 5000,
            "final_price": 0,
            "finalPrice": 5000,
            "brand": "پفک‌نمکی‌کو",
            "brand_image_src": "https://example.com/brands/saltypofco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "پفک",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 40,
            "product_name": "کیک و کلوچه",
            "product_details": "کیک و کلوچه ۲۰۰ گرمی",
            "main_price": 7000,
            "final_price": 0,
            "finalPrice": 7000,
            "brand": "کیک‌کلوچه‌کو",
            "brand_image_src": "https://example.com/brands/cakeco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "sub_category": "کیک و کلوچه",
            "category_image_src": "https://example.com/categories/snacks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 41,
            "product_name": "آب معدنی",
            "product_details": "آب معدنی ۱.۵ لیتر",
            "main_price": 2000,
            "final_price": 0,
            "finalPrice": 2000,
            "brand": "آب‌معدنی‌کو",
            "brand_image_src": "https://example.com/brands/mineralwater.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "آب معدنی",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 42,
            "product_name": "چای سیاه",
            "product_details": "چای سیاه ۴۰۰ گرمی",
            "main_price": 10000,
            "final_price": 10,
            "finalPrice": 9000,
            "brand": "چای‌کو",
            "brand_image_src": "https://example.com/brands/tea.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "چای",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 43,
            "product_name": "قهوه فوری",
            "product_details": "قهوه فوری ۱۰۰ گرمی",
            "main_price": 7000,
            "final_price": 0,
            "finalPrice": 7000,
            "brand": "قهوه‌فوری‌کو",
            "brand_image_src": "https://example.com/brands/instantcoffee.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "قهوه فوری",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 44,
            "product_name": "آبمیوه طبیعی سیب",
            "product_details": "آبمیوه طبیعی سیب ۱ لیتری",
            "main_price": 12000,
            "final_price": 0,
            "finalPrice": 12000,
            "brand": "آب‌میوه‌طبیعی‌کو",
            "brand_image_src": "https://example.com/brands/naturaljuice.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "آبمیوه",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 45,
            "product_name": "چای سبز",
            "product_details": "چای سبز ۴۰۰ گرمی",
            "main_price": 80000,
            "final_price": 5,
            "finalPrice": 76000,
            "brand": "چای‌سبز‌کو",
            "brand_image_src": "https://example.com/brands/green-tea.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "چای",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 46,
            "product_name": "کنسرو ماهی تن",
            "product_details": "کنسرو ماهی تن ۱۸۰ گرمی",
            "main_price": 80000,
            "final_price": 0,
            "finalPrice": 80000,
            "brand": "کنسرو‌ماهی‌تن‌کو",
            "brand_image_src": "https://example.com/brands/tunafish.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "کنسرو و غذای آماده",
            "sub_category": "کنسرو ماهی",
            "category_image_src": "https://example.com/categories/cannedfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 47,
            "product_name": "کنسرو سبزیجات",
            "product_details": "کنسرو سبزیجات ۴۰۰ گرمی",
            "main_price": 5000,
            "final_price": 0,
            "finalPrice": 5000,
            "brand": "کنسرو‌سبزیجات‌کو",
            "brand_image_src": "https://example.com/brands/vegetablecanned.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "کنسرو و غذای آماده",
            "sub_category": "کنسرو سبزیجات",
            "category_image_src": "https://example.com/categories/cannedfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        }, {
            "id": 48,
            "product_name": "کنسرو خوراک لوبیا",
            "product_details": "کنسرو خوراک لوبیا ۴۰۰ گرمی",
            "main_price": 6000,
            "final_price": 0,
            "finalPrice": 6000,
            "brand": "کنسرو‌لوبیا‌کو",
            "brand_image_src": "https://example.com/brands/bean-canned.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "کنسرو و غذای آماده",
            "sub_category": "خوراک‌های آماده",
            "category_image_src": "https://example.com/categories/cannedfood.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        }, {
            "id": 49,
            "product_name": "پاستا",
            "product_details": "پاستا ۵۰۰ گرمی",
            "main_price": 8000,
            "final_price": 5,
            "finalPrice": 7600,
            "brand": "پاستا‌کو",
            "brand_image_src": "https://example.com/brands/pasta.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "خواربار",
            "sub_category": "ماکارونی و رشته",
            "category_image_src": "https://example.com/categories/grocery.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        }, {
            "id": 50,
            "product_name": "دمنوش گل محمدی",
            "product_details": "دمنوش گل محمدی ۲۰ عددی",
            "main_price": 3000,
            "final_price": 0,
            "finalPrice": 3000,
            "brand": "دمنوش‌کو",
            "brand_image_src": "https://example.com/brands/herbaltea.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "دمنوش",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 51,
            "product_name": "شکر قند و نبات",
            "product_details": "شکر قند و نبات ۵۰۰ گرمی",
            "main_price": 3000,
            "final_price": 0,
            "finalPrice": 3000,
            "brand": "شکر‌کو",
            "brand_image_src": "https://example.com/brands/sugar.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "خواربار",
            "sub_category": "شکر قند و نبات",
            "category_image_src": "https://example.com/categories/grocery.jpg",
            "size": "20*20",
            "Production": "2/2024",
            "expiration_date": "5/2025"
        },
        {
            "id": 52,
            "product_name": "پودر قهوه",
            "product_details": "پودر قهوه ۲۰۰ گرمی",
            "main_price": 3000,
            "final_price": 0,
            "finalPrice": 3000,
            "brand": "قهوه‌کو",
            "brand_image_src": "https://example.com/brands/coffee.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "sub_category": "پودر قهوه",
            "category_image_src": "https://example.com/categories/drinks.jpg",
            "size": "20*20",
            "production_date": "2/2024",
            "expiration_date": "5/2025"
        }
    ];

    limit = request.GET.get('limit')
    if limit:
        try:
            limit = int(limit)
        except ValueError:
            return JsonResponse({"error": "Invalid limit value"}, status=400)

    id_param = request.GET.get('id')
    if id_param:
        try:
            id_param = int(id_param)

            data = [item for item in data if item['id'] == id_param]
        except ValueError:
            return JsonResponse({"error": "Invalid id value"}, status=400)

    if limit:
        data = data[:limit]

    return JsonResponse(data, safe=False)
