from django.db import models
from django.contrib.auth.models import BaseUserManager, User, AbstractBaseUser

class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None,*args, **kwargs):

        if not email:
            ValueError("Le champ email est obligatoire")
        if not username :

            ValueError("Le champ email est obligatoire")
        user = User.objects.create(
            username = username,
            email = self.normalize_email(email),

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, *args, **kwargs):

        user = self.create_user(
            email=email,
            username=username,
            password=password
        )
        user.is_active = True
        user.is_staff=True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)

    #required
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    

    

    REQUIRED_FIELDS = ['username',]
    USERNAME_FIELD = 'email'

    objects = UserManager()        