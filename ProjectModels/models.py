from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomManager(BaseUserManager):
    def create_user(self,email,password,**extra_kwargs):
        email = self.normalize_email(email)
        user = self.model(email = email,**extra_kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password,**extra_kwargs):
        extra_kwargs.setdefault('is_staff',True)
        extra_kwargs.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_kwargs)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=128, unique=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_otpverify = models.BooleanField(default=False)
    

    objects = CustomManager()
    USERNAME_FIELD = 'email'
    def __str__(self) -> str:
        
        return f"{self.id}_{self.email}_{self.name}"
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)

class ProfileImage(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profileimage")
    profimage = models.ImageField(null=True,blank=True,upload_to="profileImages")