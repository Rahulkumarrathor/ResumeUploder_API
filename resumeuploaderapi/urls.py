from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', views.ProfileView.as_view()),
    path('list/', views.ProfileView.as_view()),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

