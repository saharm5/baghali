import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.conf import settings
from django.views.decorators.http import require_http_methods


# Helper function to get file path safely
def get_file_path(file_name):
    return os.path.join(settings.BASE_DIR, 'myApp', 'static', file_name)


# View to handle GET requests for the plist
def plist(request):
    try:
        csv_path = get_file_path('data.csv')
        df = pd.read_csv(csv_path)
        data = df.to_json(orient='records')
        return JsonResponse(json.loads(data), safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


# View to handle POST requests for receiving messages


@csrf_exempt
@require_http_methods(["GET", "POST"])
def recievemsg(request):
    if request.method == 'GET':
        return handle_get_request(request)
    elif request.method == 'POST':
        return handle_post_request(request)


# Handle GET request
def handle_get_request(request):
    data = request.GET.get('data')
    if data:
        try:
            file_path = get_file_path('info2.txt')
            with open(file_path, 'a') as f:
                f.write(data + '\n')
            return JsonResponse({"status": "ok", "message": "Data saved successfully"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "No data received"}, status=400)


# Handle POST request
def handle_post_request(request):
    # try:
    #     data = json.loads(request.body)
    #     phone = data.get("phone")
    #     from_date = data.get("fromDate")
    #     email = data.get("email")
    #     comments = data.get("comments")
    #
    #     file_path = get_file_path('info.txt')
    #     with open(file_path, 'a') as f:
    #         f.write(f"Phone: {phone}, Date: {from_date}, Email: {email}, Comments: {comments}\n")
    #
    #     return JsonResponse({"status": "ok", "message": "Data saved successfully"})
    # except json.JSONDecodeError:
    #     return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    # except Exception as e:
    #     return JsonResponse({"status": "error", "message": str(e)}, status=500)
    try:
        data = json.loads(request.body)
        phone = data.get("phone")

        file_path = get_file_path('info2.txt')
        with open(file_path, 'a') as f:
            f.write(f"Phone: {phone}\n")

        return JsonResponse({"status": "ok", "message": "Data saved successfully"})
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

    #     try:
    #         data = json.loads(request.body)
    #         phone = data.get("phone")
    #
    #         if not phone:
    #             return JsonResponse({"status": "error", "message": "Phone number is required"}, status=400)
    #
    #         user_info = UserInfo.objects.filter(phone=phone).first()
    #
    #         if user_info:
    #             user, created = User.objects.get_or_create(username=user_info.email)
    #             token = RefreshToken.for_user(user)
    #             access_token = str(token.access_token)
    #
    #             return JsonResponse({
    #                 "status": "ok",
    #                 "message": "Phone number exists",
    #                 "token": access_token
    #             })
    #         else:
    #             return JsonResponse({"status": "error", "message": "Phone number not found"}, status=404)
    #
    #     except json.JSONDecodeError:
    #         return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    #     except Exception as e:
    #         return JsonResponse({"status": "error", "message": str(e)}, status=500)

#
# # DjangoProject1/views.py
#
# import json
# import os
# import pandas as pd
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import UserInfo
#
#
# # Helper function to get file path safely
# def get_file_path(file_name):
#     return os.path.join(settings.BASE_DIR, 'myApp', 'static', file_name)
#
#
# # View to handle GET requests for the plist
# def plist(request):
#     try:
#         csv_path = get_file_path('data.csv')
#         df = pd.read_csv(csv_path)
#         data = df.to_json(orient='records')
#         return JsonResponse(json.loads(data), safe=False)
#     except Exception as e:
#         return JsonResponse({"status": "error", "message": str(e)}, status=500)
#
#
# # View to handle POST requests for receiving messages
# @csrf_exempt
# def recievemsg(request):
#     if request.method == 'GET':
#         return handle_get_request(request)
#     elif request.method == 'POST':
#         action = request.POST.get('action')
#         if action == 'save_data':
#             return handle_save_data(request)
#         elif action == 'check_phone':
#             return handle_check_phone(request)
#         else:
#             return JsonResponse({"status": "error", "message": "Invalid action"}, status=400)
#     return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
#
#
# # Handle GET request
# def handle_get_request(request):
#     data = request.GET.get('data')
#     if data:
#         try:
#             file_path = get_file_path('info2.txt')
#             with open(file_path, 'a') as f:
#                 f.write(data + '\n')
#             return JsonResponse({"status": "ok", "message": "Data saved successfully"})
#         except Exception as e:
#             return JsonResponse({"status": "error", "message": str(e)}, status=500)
#     return JsonResponse({"status": "error", "message": "No data received"}, status=400)
#
#
# # Handle POST request to save data
# def handle_save_data(request):
#     try:
#         data = json.loads(request.body)
#         phone = data.get("phone")
#         from_date = data.get("fromDate")
#         email = data.get("email")
#         comments = data.get("comments")
#
#         file_path = get_file_path('info.txt')
#         with open(file_path, 'a') as f:
#             f.write(f"Phone: {phone}, Date: {from_date}, Email: {email}, Comments: {comments}\n")
#
#         return JsonResponse({"status": "ok", "message": "Data saved successfully"})
#     except json.JSONDecodeError:
#         return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
#     except Exception as e:
#         return JsonResponse({"status": "error", "message": str(e)}, status=500)
#
#
# # Handle POST request to check phone number and return token
# def handle_check_phone(request):
#     try:
#         data = json.loads(request.body)
#         phone = data.get("phone")
#
#         if not phone:
#             return JsonResponse({"status": "error", "message": "Phone number is required"}, status=400)
#
#         user_info = UserInfo.objects.filter(phone=phone).first()
#
#         if user_info:
#             user, created = User.objects.get_or_create(username=user_info.email)
#             token = RefreshToken.for_user(user)
#             access_token = str(token.access_token)
#
#             return JsonResponse({
#                 "status": "ok",
#                 "message": "Phone number exists",
#                 "token": access_token
#             })
#         else:
#             return JsonResponse({"status": "error", "message": "Phone number not found"}, status=404)
#
#     except json.JSONDecodeError:
#         return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
#     except Exception as e:
#         return JsonResponse({"status": "error", "message": str(e)}, status=500)
