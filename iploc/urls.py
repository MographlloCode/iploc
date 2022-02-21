from django.urls import path, include
from .views import *
from .models import *
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="IPLoc API",
      default_version='v1',
      description="Mundo DevOps",
      contact=openapi.Contact(email="gustavomello@contactgms.com")
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

ip = IP.objects.filter().order_by('-id')[0]

router = routers.DefaultRouter()
router.register('ip', InsereIp, basename='IP')
router.register('ip_dados', ListaDados, basename='IP_ Dados')


urlpatterns = [
    path('', include(router.urls,)),
    path(f'listaip/{ip}', ListaInfoIp.as_view()),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
