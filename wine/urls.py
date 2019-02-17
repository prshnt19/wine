from django.contrib.auth import views as auth_views
from  wine import views
from django.urls import path
from .views import (
	wine_detail,

	)

app_name='wine'

urlpatterns= [

    path("", wine_detail, name = "index"),
    path('register/', views.register, name = 'register'),

]
