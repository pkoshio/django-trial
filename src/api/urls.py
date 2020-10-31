from django.urls import path

from .views import QuestionApiView

urlpatterns = [
    path('', QuestionApiView.as_view())
]