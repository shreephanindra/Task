from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('signup/',views.signup,name='signup'),
    path('books/<str:na>/view',views.threed,name='threed_model'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
