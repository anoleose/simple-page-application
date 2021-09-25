from django.urls import path, include
from . import views

name_app = 'spa_app'


urlpatterns = [
	path('', views.index, name='indexviews'),
	path('filtering/', views.filtering, name='filtering'),

];