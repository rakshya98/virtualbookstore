from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('sell', views.sell),
    path('buy', views.buy),
    path('social', views.social),
    path('eng', views.english),
    path('maths', views.maths),
    path('nepali', views.nepali),
    path('science', views.science),
    path('engg', views.engg),
    path('good', views.good),
    path('fibuy/<int:id>', views.fibuy),
    path('fibuy', views.final),

]
