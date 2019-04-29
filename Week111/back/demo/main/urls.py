from django.urls import path,re_path
from main import views
urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('time/', views.current_time),
    # re_path(r'time/\d{2}/', views.current_time)
    re_path(r'time/plus/(\d{2})/', views.current_time_plus),
    path('products/<int:pk>/', views.show_product),
    path('categories/', views.category_list)
]