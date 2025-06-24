from django.urls import path
from .views import *

urlpatterns = [
    path('product_list', product_list, name='product_list'),
    path('', admin_index, name='home'), 
    path('add_product/',add_product,name='add_product'),
    path('admin/product/update/<int:product_id>/', update_product, name='update_product'),
    path('delete_product/<int:product_id>/',admin_delete_movie,name='delete_product'),
    path('add_category/',createcategories,name='add_category'),
    path('delete_category/<int:category_id>/',delete_category,name='delete_category'),
    path('logout/',logout_view,name='logout'),

]
