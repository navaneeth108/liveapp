from django.urls import path,include
from . import views
from django.contrib.auth.models import User
from .views import get_users, return_book
from .views import user_logout
from .views import SignUpView

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/register/', views.user_register, name='user_register'),
    path('user/login/', views.user_login, name='user_login'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('catalog/', views.catalog, name='catalog'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('my_books/', views.my_books, name='my_books'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('add_book/', views.add_book, name='add_book'),
    path('logout/', user_logout, name='user_logout'),
    path('get_users/', get_users, name='get_users'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('return_book/<int:record_id>/', return_book, name='return_book'),
    path('renew_book/<int:record_id>/', views.renew_book, name='renew_book'),
    path('return_book_admin/<int:record_id>/', views.return_book_admin, name='return_book_admin'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

