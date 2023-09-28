from django.db import models

# According to my understanding, I consider SKU,NAME,LOCATION,DEPARTMENT,CATEGORY,SUBCATEGORY as tables

class AppModel(models.Model):
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default = False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        abstract = True
 
class Location(AppModel):
    name = models.CharField(max_length=255,default = None)
    description = models.CharField(max_length=255,default = None)

    def __str(self):
        return self.name
    
class Department(AppModel):
    name = models.CharField(max_length=255,default = None)
    description = models.CharField(max_length=255,default = None)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE,default = None,related_name='department_location')
    def __str(self):
        return self.name

class Category(AppModel):
    name = models.CharField(max_length=255,default = None)
    description = models.CharField(max_length=255,default = None)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE,default = None,related_name='category_department')
    
    def __str(self):
        return self.name

class Subcategory(AppModel):
    name = models.CharField(max_length=255,default = None)
    description = models.CharField(max_length=255,default = None)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default = None,related_name='sub_category_category')
    def __str(self):
        return self.name 

class SKU(AppModel):
    name = models.CharField(max_length=255,default = None)
    description = models.CharField(max_length=255,default = None)
    subcategory_id = models.ForeignKey(Subcategory, on_delete=models.CASCADE,default = None,related_name='subcategory')
    def __str(self):
        return self.name 