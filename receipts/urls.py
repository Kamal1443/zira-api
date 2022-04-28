from django.urls import path
from .views import Rec_get

urlpatterns =[
    path('receipts/', Rec_get.as_view()),
]