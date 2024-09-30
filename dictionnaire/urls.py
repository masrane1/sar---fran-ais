from django.contrib import admin
from django.urls import path
from mots import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('apropos/', views.apropos, name='apropos'),
    path('entrainement/', views.entrainement, name='entrainement'),
]

