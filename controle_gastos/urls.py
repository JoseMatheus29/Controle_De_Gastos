from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from contas.views import  transacao, novatransacao, atualizar, deletar
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', transacao, name='transacao'),
    path('novatransacao/', novatransacao , name = 'urlnova'),
    path('atualizar/<int:pk>', atualizar, name = 'atualizar'),
    path('deletar/<int:pk>', deletar, name = 'deletar'),
    path('contas/', include('django.contrib.auth.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
