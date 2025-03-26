from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.static import serve

def redirect_to_login(request):
    return redirect('account_login')

def redirect_to_signup(request):
    return redirect('account_signup')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('login/', redirect_to_login),
    path('register/', redirect_to_signup),
    path('dashboard/', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    path('accounts/profile/', login_required(TemplateView.as_view(template_name='profile.html')), name='profile'),
    # Маршрут для обслуживания CSS из папки templates
    path('styles.css', serve, {'document_root': 'app/templates', 'path': 'css/styles.css'}),
]
