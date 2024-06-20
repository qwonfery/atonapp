from django.contrib import admin
from django.urls import path
from users.views import login_view
from clients.views import client_list,  update_client_status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('clients/', client_list, name='client_list'),
    path('clients/<int:client_id>/status/', update_client_status, name='update_client_status'),
]
