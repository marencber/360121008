from django.urls import path

from post.views import post_create, post_delete, post_details, post_index, post_update
 


urlpatterns = [
    path('about/', post_index),
    path('details/', post_details),
    path('create/', post_create),
    path('update/', post_update),
    path('delete/', post_delete)
    

]
