from django.db import models
from utils.models import BaseModel

# Create your models here.

class Register(BaseModel):
    user_name= models.CharField(max_length=255)
    user_phone= models.CharField(max_length=9)
    user_email=  models.CharField(max_length=255)
    user_password=models.CharField(max_length=255)

class News(BaseModel):
    post_img= models.ImageField(upload_to="product_images")
    post_data= models.CharField(max_length=30)
    post_title= models.CharField(max_length=255)
    post_description= models.CharField(max_length=255)


class Books(BaseModel):
    book_img= models.ImageField(upload_to="product_images")
    book_data= models.CharField(max_length=30)
    book_title= models.CharField(max_length=255)
    book_description= models.CharField(max_length=255)
    book_author= models.CharField(max_length=255)
    book_category= models.CharField(max_length=255)
    book_language= models.CharField(max_length=255)
    book_count= models.CharField(max_length=255)

class Course(BaseModel):
    course_img= models.ImageField(upload_to="product_images")
    course_section= models.CharField(max_length=30)
    course_title= models.CharField(max_length=255)
    course_description= models.CharField(max_length=255)
    course_author= models.CharField(max_length=255)
    course_category= models.CharField(max_length=255)
    course_language= models.CharField(max_length=255)
    course_count= models.CharField(max_length=255)
    
class Profile(BaseModel):
    profile_img= models.ImageField(upload_to="product_images")
    profile_fullname= models.CharField(max_length=255)
    profile_brithday= models.CharField(max_length=255)
    profile_phone= models.CharField(max_length=255)
    profile_password= models.CharField(max_length=255)
