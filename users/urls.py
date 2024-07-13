from django.urls import path # type: ignore
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('users/list/', views.user_list, name='users_list'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('user/todos/<int:user_id>/', views.todos, name='todos'),
    path('user/new_todos/<int:user_id>/',views.new_todos, name='new_todos'),
    path('user/update_todo/<int:todo_id>/',views.toggle_todo_state, name='toggle_todos'),
    path('user/change_todo/<int:todo_id>/',views.change_todo, name='change_ todo'),
    path('user/delete_todo/<int:todo_id>/',views.delete_todo, name='delete_todo')    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

