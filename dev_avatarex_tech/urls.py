from django.urls import path, include

urlpatterns = [
    path('fail-safe-system/', include('fss.urls')),
]
