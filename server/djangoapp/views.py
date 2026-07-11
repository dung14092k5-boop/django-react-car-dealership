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
from django.http import JsonResponse

def get_dealer_reviews(request, dealer_id):
    # Code giả lập data hoặc gọi sang express backend của bạn
    data = [{"dealership": dealer_id, "name": "Reviewer Test", "review": "Good product"}]
    return JsonResponse(data, safe=False)

def get_dealers(request):
    # Code giả lập hoặc gọi sang Express backend của bạn
    data = [{"id": 1, "name": "Toyota Dealer One", "city": "New York"}]
    return JsonResponse(data, safe=False)
# Giữ nguyên các hàm cũ (login_user, logout_user, get_dealers...) và thêm hàm này xuống cuối file:

def get_dealer_details(request, dealer_id):
    # Trả về dữ liệu giả lập chi tiết dealer dựa theo dealer_id truyền vào
    # (Sau này lab sẽ hướng dẫn bạn fetch từ Node.js Express backend)
    data = {
        "id": dealer_id, 
        "name": f"Toyota Dealer {dealer_id}", 
        "city": "New York", 
        "state": "Kansas"
    }
    return JsonResponse(data, safe=False)