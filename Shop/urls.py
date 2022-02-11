from xml.dom.minidom import Document
from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

app_name='Shop'

urlpatterns =[
    path('', views.product_list,name='Product_List'),
    path('<slug:category_slug>/', views.product_list, name='Product_List_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='Product_Detail'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)