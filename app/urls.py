from django.urls import path
from .import views

urlpatterns = [
    path('',views.Index,name="index"),
    path('loginpage/',views.LoginPage,name="loginpage"),
    path('signuppage/',views.Signuppage,name="signpage"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name='signup'),
    path('detail/',views.Detail_form,name="detail_from"),
    path('location/grid/', views.location_grid, name='location_grid')
]