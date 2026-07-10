from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Trường hợp test bằng cURL qua Form data (-d)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Trường hợp nhận dữ liệu dạng JSON (từ React frontend sau này)
        if not username:
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
            except:
                pass

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"username": username, "status": "Authenticated"})
        else:
            return JsonResponse({"username": username, "status": "Authentication Failed"})
            
    return JsonResponse({"error": "Method not allowed"}, status=405)

from django.contrib.auth import logout

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"username": ""})