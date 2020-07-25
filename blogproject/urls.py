from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('main/', blog.views.main, name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

