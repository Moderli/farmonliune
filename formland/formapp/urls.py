from django.urls import path
from .views import signup, login_view, user_logout, profile_setup, home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),

    path('profile_setup/', profile_setup, name='profile_setup'),
    path('', home, name='home'),    # Add other URLs as needed
    path('logout/', user_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
