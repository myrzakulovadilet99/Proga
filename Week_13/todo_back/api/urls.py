from django.urls import path, re_path
from api import views

# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:num>/', views.task_list_num),
#     # path('task_lists/<int:num>/tasks', views.task_list_tasks)
# ]

#
urlpatterns = [
    path('task_lists/', views.Tasklist.as_view()),
    path('task_lists/<int:pk>/', views.Tasklist_detail.as_view()),
    path('task_lists/<int:num>/tasks', views.Task.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.Login),
    path('logout/', views.logout)
]



