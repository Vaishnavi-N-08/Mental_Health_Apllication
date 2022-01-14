from django.urls import path 
from . import views


urlpatterns = [    
    path('feed',views.feed,name='feed'),
    path('base',views.base,name='base'),
    path('',views.trail,name='trail'),
    path('feed',views.feed,name='feed'),
    path('exercise',views.exercise,name='exercise'),
    path('register',views.register,name='register'),
    path('logout', views.logout,name="logout"),  
    path('ex1',views.ex1,name='ex1'),
    path('ex2',views.ex2,name='ex2'),
    path('ex3',views.ex3,name='ex3'),
    path('ex4',views.ex4,name='ex4'),
    path('ex5',views.ex5,name='ex5'),
    path('ex6',views.ex6,name='ex6'),
    path('ex7',views.ex7,name='ex7'),
    path('ex8',views.ex8,name='ex8'),
    path('ex9',views.ex9,name='ex9'),
    path('ex10',views.ex10,name='ex10'),
    path('test', views.test,name="test"),  
    path('result', views.result,name="result"),
    path('review', views.review,name="review"),
    path('feedback', views.feedback,name="feedback"),
    
]