import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from django.conf import settings


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
@csrf_exempt  # Disable CSRF protection for testing (re-enable for production)
def recievemsg(request):
    if request.method == 'GET':
        return handle_get_request(request)
    elif request.method == 'POST':
        return handle_post_request(request)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


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
    try:
        data = json.loads(request.body)
        phone = data.get("phone")
        from_date = data.get("fromDate")
        email = data.get("email")
        comments = data.get("comments")

        file_path = get_file_path('info.txt')
        with open(file_path, 'a') as f:
            f.write(f"Phone: {phone}, Date: {from_date}, Email: {email}, Comments: {comments}\n")

        return JsonResponse({"status": "ok", "message": "Data saved successfully"})
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
