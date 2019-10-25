from django.urls import path
from rest_framework.routers import DefaultRouter
from todos_app import api


router = DefaultRouter()
router.register('todo', api.TodoModelViewSet, base_name='todo')

urlpatterns = []
urlpatterns += router.urls

# urlpatterns = [
#     path('todo/', api.TodoListView.as_view(), name='todo_list'),
#     path('todo/<int:todo_id>/', api.TodoDetailView.as_view(), name='todo_detail')
# ]

