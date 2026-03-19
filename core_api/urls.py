from django.urls import path, include
from .routers import router


urlpatterns = [
    path('api-luis/', include(router.urls)),
    
]
