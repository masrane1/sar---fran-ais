from django.contrib import admin
from django.urls import path
from mots import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('apropos/', views.apropos, name='apropos'),
    path('entrainement/', views.entrainement, name='entrainement'),
]

