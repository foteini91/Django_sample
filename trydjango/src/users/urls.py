from django.urls import path
from . import views

urlpatterns = [
    path('names/', views.get_all_names, name= 'all_names'),
    path('names/1/', views.get_name_by_id, name='name_by_id'),
    path(r'name/1/', views.delete_name_by_id, name='delete_name'),
    path('name/<str:name>/', views.post_name, name='post_name'),
    path('putname/<int:id>/<str:name>', views.put_name, name='put_name'),    

    ## I tried the following url but i get an error
    #path('name/<int:id>/', views.delete_name_by_id, name='delete_name_by_id'), 
    #path('names/<int:id>/', views.get_name_by_id, name='name_by_id')
   

]