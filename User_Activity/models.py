from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from jsonfield import JSONField


class UserActManager(BaseUserManager):
    def create_user(self,email,username,real_name,password=None):
        if not email:
            raise ValueError("Email is mandatory")
        if not username:
            raise ValueError("Username is mandatory")
        if not real_name:
            raise ValueError("Real Name is mandatory")

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            real_name=real_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,username,real_name,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            real_name=real_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using = self._db)
        return user


class UserAct(AbstractBaseUser):
    id=models.CharField(max_length=50, verbose_name='id')
    email=models.EmailField(unique=True)
    real_name=models.CharField(max_length=50)
    username=models.CharField(max_length=20,primary_key=True, unique=True)
    list_act = JSONField(default=[],verbose_name='activity_periods')
    is_active = models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password','real_name']

    objects = UserActManager()

    def __str__(self):
        return self.real_name

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

