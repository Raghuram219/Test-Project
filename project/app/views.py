from django.shortcuts import render
from rest_framework import viewsets
from .models import Location,Department,Category,Subcategory,SKU
from .serializers import LocationSerializer,DepartmentSerializer,CategorySerializer,SubcategorySerializer,SKUSerializer
import django_filters
from django_filters import rest_framework as filters_
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication


class SKUFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    subcategory = django_filters.CharFilter(
        field_name='subcategory_id__name',
        lookup_expr='icontains',
        label='Subcategory Name'
    )
    category = django_filters.CharFilter(
        field_name='subcategory_id__category_id__name',
        lookup_expr='icontains',
        label='Category Name'
    )
    department = django_filters.CharFilter(
        field_name='subcategory_id__category_id__department_id__name',
        lookup_expr='icontains',
        label='Department Name'
    )
    location = django_filters.CharFilter(
        field_name='subcategory_id__category_id__department_id__location_id__name',
        lookup_expr='icontains',
        label='Location Name'
    )

    class Meta:
        model = SKU
        fields = ['name', 'subcategory', 'category','department','location']

class LocationViewset(viewsets.ModelViewSet):
    queryset = Location.objects.filter(is_deleted=False)
    serializer_class = LocationSerializer

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.filter(is_deleted=False)
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.AllowAny,)

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer

class SubcategoryViewset(viewsets.ModelViewSet):
    queryset = Subcategory.objects.filter(is_deleted=False)
    serializer_class = SubcategorySerializer

class SKUViewset(viewsets.ModelViewSet):
    queryset = SKU.objects.filter(is_deleted=False)
    serializer_class = SKUSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('id', 'date_created')
    ordering_fields = ('id', 'date_created')
    ordering = ('id')
    filterset_class = SKUFilterSet
