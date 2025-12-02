from django.urls import path
from . import views

app_name = 'freddyapp'


# Rutas de la aplicación
urlpatterns = [
    path('', views.animatronic_list, name='list'),
    path('list/', views.animatronic_list, name='list'),
    path('new/', views.animatronic_new, name='new'),
    path('<int:id>/view/', views.animatronic_view, name='view'),
    path('<int:id>/edit/', views.AnimatronicUpdate.as_view(), name='edit'),
    path('<int:id>/delete/', views.AnimatronicDelete.as_view(), name='delete'),
    path('newuser/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('theme/', views.set_dark_theme, name='theme'),
    path('clearcookies/', views.clear_theme_cookie, name='clearcookies'),
]