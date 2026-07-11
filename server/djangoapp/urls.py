from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Giao diện chính React tĩnh
    # Sửa dòng path trống thành dòng này:
    path('', TemplateView.as_view(template_name="Home.html"), name='index'),
    
    # Các API xử lý Authentication
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    
    # Các API lấy dữ liệu backend
    path('get_dealers', views.get_dealers, name='get_dealers'),
    path('get_reviews/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    
    # Khai báo đường dẫn chi tiết dealer (Task 10)
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
]