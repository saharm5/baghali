from django.http import JsonResponse


def get_data_categories(request):
    categories = [
        {
            "imageSrc": "kharbar.png",
            "categoryName": "خواربار",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/snacks.png?raw=true",
            "categoryName": "تنقلات",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/dairy.png?raw=true",
            "categoryName": "لبنیات",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/drinks.png?raw=true",
            "categoryName": "نوشیدنی ها",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/cleaning.png?raw=true",
            "categoryName": "نظافت منزل",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/condiments.png?raw=true",
            "categoryName": "چاشنی و ادویه",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/canned.png?raw=true",
            "categoryName": "کنسرو و غذای آماده",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/cosmetics.png?raw=true",
            "categoryName": "آرایشی و بهداشتی",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/protein.png?raw=true",
            "categoryName": "محصولات پروتئینی",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/home.png?raw=true",
            "categoryName": "خانه و سبک زندگی",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/nuts.png?raw=true",
            "categoryName": "آجیل و خشکبار",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/mother-and-child.png?raw=true",
            "categoryName": "مادر و کودک",
            "categoryLink": "#"
        },
        {
            "imageSrc": "https://github.com/saharm5/react-apps/blob/main/src/assets/Img/fruits-and-vegetables.png?raw=true",
            "categoryName": "میوه و سبزیجات",
            "categoryLink": "#"
        }
    ];

    return JsonResponse(categories,safe=False)
