from django.http import JsonResponse


def get_data(request):
    data = [
        {
            "id": 1,
            "productName": "چیپس نمکی",
            "productDetails": "بسته ۱۰۰ گرمی چیپس طعم نمک",
            "mainPrice": "۲۰,۰۰۰ تومان",
            "discount": "۱۰٪",
            "finalPrice": "۱۸,۰۰۰ تومان",
            "brand": "چی توز",
            "brandImageSrc": "https://logoyab.com/wp-content/uploads/2024/06/Cheetoz-Logo-450x450.png",
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
            "subCategory": "چیپس و پفک",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 2,
            "productName": "پفک نمکی",
            "productDetails": "بسته ۵۰ گرمی پفک نمکی",
            "mainPrice": "۵,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۴,۷۵۰ تومان",
            "brand": "چی توز",
            "brandImageSrc": "https://logoyab.com/wp-content/uploads/2024/06/Cheetoz-Logo-450x450.png",
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
            "subCategory": "چیپس و پفک",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 3,
            "productName": "شکلات تلخ",
            "productDetails": "شکلات تلخ ۹۰ درصد، بسته ۱۵۰ گرمی",
            "mainPrice": "۱۵۰,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۱۵۰,۰۰۰ تومان",
            "brand": "آیدین",
            "brandImageSrc": "https://example.com/brands/chocolatco.png",
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
            "subCategory": "شکلات و آبنبات",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 4,
            "productName": "پاستیل رنگی",
            "productDetails": "بسته ۲۰۰ گرمی پاستیل رنگی",
            "mainPrice": "۸,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۷,۶۰۰ تومان",
            "brand": "شیبا",
            "brandImageSrc": "https://logoyab.com/wp-content/uploads/2024/06/Shiba-Logo-1030x1030.png",
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
            "subCategory": "پاستیل و آدامس",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 5,
            "productName": "کیک شکلاتی",
            "productDetails": "کیک شکلاتی ۴۰۰ گرمی",
            "mainPrice": "۱۰,۰۰۰ تومان",
            "discount": "۱۰٪",
            "finalPrice": "۹,۰۰۰ تومان",
            "brand": "درنا",
            "brandImageSrc": "https://tiktarh.com/wp-content/uploads/2024/07/RLg1001001www.tiktarh.com_.jpg",
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
            "subCategory": "کیک و کلوچه",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 6,
            "productName": "آبنبات نعنا",
            "productDetails": "آبنبات نعنا ۲۹ گرمی",
            "mainPrice": "۴,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۴,۰۰۰ تومان",
            "brand": "منتوس",
            "brandImageSrc": "https://banner2.cleanpng.com/20180713/evf/aaww3wif1.webp",
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
            "subCategory": "شکلات و آبنبات",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 7,
            "productName": "لواشک میوه‌ای",
            "productDetails": "لواشک میوه‌ای ۱۵۰ گرمی",
            "mainPrice": "۵,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۴,۷۵۰ تومان",
            "brand": "نازلی",
            "brandImageSrc": "https://example.com/brands/fruitco.png",
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
            "subCategory": "لواشک و آلوچه",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 8,
            "productName": "تخمه آفتابگردان",
            "productDetails": "تخمه آفتابگردان ۴۰ گرمی",
            "mainPrice": "۳,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۳,۰۰۰ تومان",
            "brand": "مزمز",
            "brandImageSrc": "https://logoyab.com/wp-content/uploads/2023/12/%D9%84%D9%88%DA%AF%D9%88-%D9%85%D8%B2%D9%85%D8%B2-450x450.png",
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
            "subCategory": "تخمه و مغزیجات طعم دار",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 9,
            "productName": "مینی تست مخصوص",
            "productDetails": "مینی تست مخصوص پرونان نان آوران مقدار 400 گرم",
            "mainPrice": "۴۰,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۴۰,۰۰۰ تومان",
            "brand": "نان آوران",
            "brandImageSrc": "https://example.com/brands/breadco.png",
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
            "subCategory": "نان",
            "categoryImageSrc": "https://example.com/categories/groceries.jpg"
        },
        {
            "id": 10,
            "productName": "شکر سفید",
            "productDetails": "شکر سفید الماس دانه - 1 کیلوگرم",
            "mainPrice": "۴۰,۵۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۴۰,۵۰۰ تومان",
            "brand": "الماس دانه",
            "brandImageSrc": "https://example.com/brands/sugarco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/dba25b58eb5b78d2cbf41d5befd49e5f5f64b5e4_1730022468.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/ddef5cca3be676317afd07367c48b4cbbfbcb111_1719947137.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/12881b5e1643b33a33570e0e21476a205cd03bf0_1723032327.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
            ],
            "category": "خواربار",
            "subCategory": "شکر قند و نبات",
            "categoryImageSrc": "https://example.com/categories/groceries.jpg"
        },
        {
            "id": 11,
            "productName": "روغن مایع",
            "productDetails": "روغن آفتابگردان حاوی توکوفرول غنچه پلاس - 1500 میلی لیتر",
            "mainPrice": "۹۵,۰۰۰ تومان",
            "discount": "۱۰٪",
            "finalPrice": "۸۵,۵۰۰ تومان",
            "brand": "غنچه",
            "brandImageSrc": "https://example.com/brands/oilco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/6ea8d1688bd9dda01dc7f5716bb7c84e9d9c3a0d_1652694148.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-comment-files/809aadaccdf35d0730b76236ebc66561649050f0_1668247019.jpg?x-oss-process=image/resize,m_lfit,h_1024,w_1024/quality,q_80"},
            ],
            "category": "خواربار",
            "subCategory": "روغن و چربی",
            "categoryImageSrc": "https://example.com/categories/groceries.jpg"
        },
        {
            "id": 12,
            "productName": "برنج ایرانی",
            "productDetails": "برنج صدری هاشمی ۵ کیلویی",
            "mainPrice": "۶۰۰,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۵۷۰,۰۰۰ تومان",
            "brand": "آقاجانیان",
            "brandImageSrc": "https://example.com/brands/riceco.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773600.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773596.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/112773607.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "خواربار",
            "subCategory": "برنج و حبوبات",
            "categoryImageSrc": "https://example.com/categories/groceries.jpg"
        },
        {
            "id": 13,
            "productName": "ماکارونی",
            "productDetails": "ماکارونی فرمی پنه کوچک مانا ۵۰۰ گرمی",
            "mainPrice": "۶۰,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۵۷,۰۰۰ تومان",
            "brand": "مانا",
            "brandImageSrc": "https://logoyab.com/wp-content/uploads/2024/06/Mana-Logo-450x450.png",
            "SubproductImages": [
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/0a7a3c51ece41abeb5251843ce8ac5eb09f792bc_1716639637.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/931030949518a53daad7029f5a7af5754e0a11a3_1716639640.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
                {
                    "productImageSrc": "https://dkstatics-public.digikala.com/digikala-products/8366dba81ba05c1612e894f66fb4bf7568655ba3_1716639642.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90"},
            ],
            "category": "خواربار",
            "subCategory": "ماکارونی و پاستا",
            "categoryImageSrc": "https://example.com/categories/groceries.jpg"
        },
        {
            "id": 14,
            "productName": "پنیر پیتزا",
            "productDetails": "پنیر پیتزا مطهر  1 کیلوگرم",
            "mainPrice": "۳۸۷,۳۹۰ تومان",
            "discount": "۲۵٪",
            "finalPrice": "۲۹۲,۲۰۰ تومان",
            "brand": "مطهر",
            "brandImageSrc": "https://example.com/brands/cheeseco.png",
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
            "subCategory": "پنیر",
            "categoryImageSrc": "https://example.com/categories/dairy.jpg"
        },
        {
            "id": 15,
            "productName": "شیر کم چرب",
            "productDetails": "شیر کم چرب ۱ لیتر",
            "mainPrice": "۶,۰۰۰ تومان",
            "discount": "۱۰٪",
            "finalPrice": "۵,۴۰۰ تومان",
            "brand": "شیرکو",
            "brandImageSrc": "https://example.com/brands/milco.png",
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
            "subCategory": "شیر",
            "categoryImageSrc": "https://example.com/categories/dairy.jpg"
        },
        {
            "id": 16,
            "productName": "خامه پاستوریزه",
            "productDetails": "خامه پاستوریزه ۲۰۰ گرمی",
            "mainPrice": "۹,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۹,۰۰۰ تومان",
            "brand": "خامه‌کو",
            "brandImageSrc": "https://example.com/brands/creamco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات لبنی",
            "subCategory": "خامه",
            "categoryImageSrc": "https://example.com/categories/dairy.jpg"
        },
        {
            "id": 17,
            "productName": "تخم مرغ",
            "productDetails": "تخم مرغ ۱۲ عددی",
            "mainPrice": "۸,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۷,۶۰۰ تومان",
            "brand": "تخم‌مرغ‌کو",
            "brandImageSrc": "https://example.com/brands/eggco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "subCategory": "تخم مرغ",
            "categoryImageSrc": "https://example.com/categories/protein.jpg"
        },
        {
            "id": 18,
            "productName": "گوشت مرغ",
            "productDetails": "گوشت مرغ ۱ کیلوگرم",
            "mainPrice": "۳۰,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۳۰,۰۰۰ تومان",
            "brand": "مرغ‌کو",
            "brandImageSrc": "https://example.com/brands/chickenco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "subCategory": "گوشت و مرغ",
            "categoryImageSrc": "https://example.com/categories/protein.jpg"
        },
        {
            "id": 19,
            "productName": "ماهی قزل‌آلا",
            "productDetails": "ماهی قزل‌آلا ۵۰۰ گرمی",
            "mainPrice": "۴۰,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۳۸,۰۰۰ تومان",
            "brand": "ماهی‌کو",
            "brandImageSrc": "https://example.com/brands/fishco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات پروتئینی",
            "subCategory": "ماهی و میگو",
            "categoryImageSrc": "https://example.com/categories/protein.jpg"
        },
        {
            "id": 20,
            "productName": "پنیر فتا",
            "productDetails": "پنیر فتا ۲۵۰ گرمی",
            "mainPrice": "۱۲,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۱۲,۰۰۰ تومان",
            "brand": "پنیر‌کو",
            "brandImageSrc": "https://example.com/brands/cheeseco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "محصولات لبنی",
            "subCategory": "پنیر",
            "categoryImageSrc": "https://example.com/categories/dairy.jpg"
        }, {
            "id": 21,
            "productName": "ماکارونی پنیری",
            "productDetails": "ماکارونی پنیری ۴۰۰ گرمی",
            "mainPrice": "۸,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۸,۰۰۰ تومان",
            "brand": "ماکارونی‌پنیری‌کو",
            "brandImageSrc": "https://example.com/brands/pastapastico.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "غذای آماده",
            "subCategory": "ماکارونی",
            "categoryImageSrc": "https://example.com/categories/readyfood.jpg"
        },
        {
            "id": 22,
            "productName": "پفک رنگی",
            "productDetails": "پفک رنگی ۵۰ گرمی",
            "mainPrice": "۶,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۵,۷۰۰ تومان",
            "brand": "پفکو",
            "brandImageSrc": "https://example.com/brands/pofco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "تنقلات",
            "subCategory": "پفک و چیپس",
            "categoryImageSrc": "https://example.com/categories/snacks.jpg"
        },
        {
            "id": 23,
            "productName": "آبمیوه طبیعی",
            "productDetails": "آبمیوه طبیعی ۱ لیتر",
            "mainPrice": "۱۰,۰۰۰ تومان",
            "discount": "۱۰٪",
            "finalPrice": "۹,۰۰۰ تومان",
            "brand": "آبمیوه‌کو",
            "brandImageSrc": "https://example.com/brands/juiceco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "نوشیدنی",
            "subCategory": "آبمیوه و نوشیدنی‌های طبیعی",
            "categoryImageSrc": "https://example.com/categories/drinks.jpg"
        },
        {
            "id": 24,
            "productName": "مربای توت فرنگی",
            "productDetails": "مربای توت فرنگی ۴۰۰ گرمی",
            "mainPrice": "۶,۰۰۰ تومان",
            "discount": "۵٪",
            "finalPrice": "۵,۷۰۰ تومان",
            "brand": "مرباکو",
            "brandImageSrc": "https://example.com/brands/jamco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "مربا و عسل",
            "subCategory": "مربا",
            "categoryImageSrc": "https://example.com/categories/jam.jpg"
        },
        {
            "id": 25,
            "productName": "عسل طبیعی",
            "productDetails": "عسل طبیعی ۳۰۰ گرمی",
            "mainPrice": "۱۵,۰۰۰ تومان",
            "discount": "۰٪",
            "finalPrice": "۱۵,۰۰۰ تومان",
            "brand": "عسل‌کو",
            "brandImageSrc": "https://example.com/brands/honeyco.png",
            "SubproductImages": [
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"},
                {"productImageSrc": "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"}
            ],
            "category": "مربا و عسل",
            "subCategory": "عسل",
            "categoryImageSrc": "https://example.com/categories/jam.jpg"
        }
    ];

    limit = request.GET.get('limit')

    # If 'limit' is provided, convert it to an integer and limit the data
    if limit:
        try:
            limit = int(limit)
            data = data[:limit]
        except ValueError:
            return JsonResponse({"error": "Invalid limit value"}, status=400)

    return JsonResponse(data, safe=False)
