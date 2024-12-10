from django.conf import settings
from django.conf.urls.static import static

from .views import landing_page, home_page
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('home/', home_page, name="home_page"),
    path("users/", include("users.user_url")),
    path("books/", include("books.book_url")),
    path("api/", include("api.url")),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)