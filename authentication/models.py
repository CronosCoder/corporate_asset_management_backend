from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name,description, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            description = description,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,name,description, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            description=description
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Company(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    description = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','description']

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self) -> str:
        return f"{self.name}"    


