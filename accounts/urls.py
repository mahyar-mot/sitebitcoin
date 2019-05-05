from django.urls import path
from .views import SignUp_View, Profile_View, SignOut_View, SignIn_View

urlpatterns = [
    path('signup/', SignUp_View.as_view(), name='signup'),
    path('login/', SignIn_View.as_view(), name='signin'),
    path('signout/', SignOut_View.as_view(), name='signout'),
    path('profile/', Profile_View.as_view() , name='profile'),
]
