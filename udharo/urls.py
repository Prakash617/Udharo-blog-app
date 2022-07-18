from django.urls import path
from .import views


urlpatterns = [
   
    path('',views.Home.as_view(), name='home'),
    path('detail/<int:id>/',views.Detail.as_view(), name='detail'),
    # path('detail/',views.Detail.as_view(), name='detail'),
    path('delete/<int:id>/',views.Delete.as_view(), name='delete'),
    path('edit/<int:id>/',views.Edit.as_view(), name='edit'),
  
 

    
]