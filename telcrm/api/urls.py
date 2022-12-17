from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'tg_user', views.UsersViewSet)
router.register(r'conversation', views.ConversationViewSet)
router.register(r'offer', views.OfferViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'template', views.TemplateViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'message', views.MessageViewSet)
router.register(r'p_task', views.PTaskViewSet)
router.register(r'd_task', views.DTaskViewSet)
router.register(r'month_task', views.Month_TaskViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('resender/<pk>', views.ResenderViewSet.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]