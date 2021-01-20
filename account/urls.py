from django.urls import path
from .views import SignUpView, Logout, login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='register'),
]
