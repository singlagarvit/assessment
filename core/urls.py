from django.urls import path
from .views import index, upload_files, orders

app_name = 'core'

urlpatterns = [
	path('', index, name='index'),
	path('orders/', orders, name='orders'),
	path('upload-files/<int:order_id>/', upload_files, name='files'),
]