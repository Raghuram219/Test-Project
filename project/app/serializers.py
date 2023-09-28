from rest_framework import serializers
from .models import Location,Department,Category,Subcategory,SKU

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class SKUSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = SKU
        fields = ('id','name','location','department','category','subcategory')

    def get_location(self, obj):
        location = obj.subcategory_id.category_id.department_id.location_id.name
        return location
    
    def get_department(self, obj):
        department = obj.subcategory_id.category_id.department_id.name
        return department

    def get_category(self, obj):
        subcategory = obj.subcategory_id.category_id.name
        return subcategory

    def get_subcategory(self, obj):
        subcategory = obj.subcategory_id.name
        return subcategory
