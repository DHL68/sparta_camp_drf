from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    # product 에 해당하는 id 경로 지정 / 순서 중요!!
    path('<product_id>/', views.ProductView.as_view()),
]