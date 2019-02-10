from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    # path('passwordchange', views.passwordchange, name='passwordchange'),
    # path('passw/<str:uidb64>/<str:token>', views.password, name='pasword'),
    path('pasw/', include('password_reset.urls')),
    path('profile/(<str:username>', views.get_user_profile, name='profile'),
]
