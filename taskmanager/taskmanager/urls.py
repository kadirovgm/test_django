
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url

# from django.views.generic import RedirectView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    url(r'^blog/', include('blog.urls')),

]


# urlpatterns += [
#    path('', RedirectView.as_view(url='/main/', permanent=True)),
# ]
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
