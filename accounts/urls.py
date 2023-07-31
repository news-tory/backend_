from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('login/', login),
    # path('signup/', signup),
    # path('logout/', logout),

    # google login
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
    path('google/login/finish/', GoogleLogin.as_view(), name='google_login_todjango'),
]