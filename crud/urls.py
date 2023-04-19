from django.urls import path
from crud import views

urlpatterns = [
    # path(r"api/create-quiz", views.CreateQuiz.as_view()),
    path(r"api/post", views.PostView.as_view()),
    path(r"api/post/<int:pk>", views.PostDetailView.as_view()),

]
