from django.urls import path
from rest_framework import routers
from .views import LocationViewset,DepartmentViewset,CategoryViewset,SubcategoryViewset,SKUViewset
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()


router.register('location',LocationViewset,basename='location')
router.register('department',DepartmentViewset,basename='department')
router.register('category',CategoryViewset,basename='category')
router.register('subcategory',SubcategoryViewset,basename='subcategory')
router.register('sku',SKUViewset,basename='sku')

urlpatterns = router.urls 

urlpatterns +=[
    path('api-token-auth/',obtain_jwt_token),
] 



