from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quetions/', views.QuestionList.as_view()),
    path('quetions/<int:pk>/', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)