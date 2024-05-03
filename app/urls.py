from django.urls import path
from .views import ApiOverview, ApiTaskList, ApiTaskDetail

urlpatterns = [
    path('', ApiOverview.as_view(), name='apioverview'),
    path('notes/', ApiTaskList.as_view(), name='apitasklist'),
    path('notes/<str:pk>/', ApiTaskDetail.as_view(), name='apitaskdetail'),
]