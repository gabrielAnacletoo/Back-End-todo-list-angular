from rest_framework import routers

from .views import TaskViewSet

app_name = "tasks"
router = routers.SimpleRouter()
router.register("", TaskViewSet, basename="tasks")
urlpatterns = router.urls 
#     path("", TasksListView.as_view(), name="tasks"),
#     path("<int:pk>/", TaskDetailsView.as_view(), name="task-details"),

# ]