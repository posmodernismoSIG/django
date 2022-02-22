from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name= "index"),
    path("<int:question_id>/detail/333", views.detail, name= "detail"),
    path("<int:question_id>/resoult", views.resoult, name= "resolut"),
    path("<int:question_id>/vote", views.vote, name= "vote")
]

