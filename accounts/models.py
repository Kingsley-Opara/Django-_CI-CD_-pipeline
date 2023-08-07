from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# Create your models here.

class UsersManager(BaseUserManager):
    
    def create_user(self, username, email, password= None, **other_fields):
        other_fields.setdefault('is_active', True)

        # if not other_fields.get('active'):
        #     raise ValueError('All users must have an active account')
        if not username:
            raise ValueError('Username is required to creat an account')
        if not email:
            raise ValueError('An Email address is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email = email, password =password, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, email, password= None, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if not other_fields.get('is_staff'):
            raise ValueError('All staff must have a staff account')
        user = self.create_user(
            username = username,
            email = email,
            password = password, 
            **other_fields
        )
        user.save(using=self._db)
        return user    

    def create_superuser(self, username, email, password =None,  **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        if not other_fields.get('is_staff'):
            raise ValueError('All staff must have a staff account')
        if not other_fields.get('is_superuser'):
            raise ValueError('All admin users must have an admin account')
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **other_fields
        )
        user.save(using=self._db)
        return user
        

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UsersManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
