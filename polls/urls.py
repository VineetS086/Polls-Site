from django.urls import path

from . import views

app_name = "Polls"

urlpatterns = [
    path('', views.Polls_list_view.as_view(), name = "List_View"),
    path('<int:id>/', views.Polls_detail_view.as_view(), name = "Detail_View"),
    path('<int:id>/vote/', views.Vote, name = "Vote"),
    
]
