from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework import serializers


class MyAccountManager( BaseUserManager ):
    def create_user(self, email, username, first_name, password=None):
        if not email:
            raise ValueError( 'Enter an email' )
        if not username:
            raise ValueError( 'Enter an username' )

        user = self.model(
            email=self.normalize_email( email ),
            username=username,
            first_name=first_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name)

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user


# Create your models here.
class Users( AbstractBaseUser ):
    username = models.CharField( max_length=255, unique=True )
    email = models.EmailField( max_length=30, unique=True, verbose_name='email' )
    date_joined = models.DateTimeField( verbose_name='date joined', auto_now_add=True )
    last_login = models.DateTimeField( verbose_name='last login', auto_now_add=True )
    is_active = models.BooleanField( default=True )
    is_admin = models.BooleanField( default=False )
    is_staff = models.BooleanField( default=False )
    is_superuser = models.BooleanField( default=False )
    first_name = models.CharField( max_length=50, verbose_name='first name' )
    last_name = models.CharField( max_length=50, verbose_name='last name' )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Recipes( models.Model ):
    name = models.CharField( max_length=255, null=False )
    user = models.ForeignKey( Users, on_delete=models.CASCADE, related_name='user_recipe' )
    # ingredients_set ([] --> list) --> all the ingredients in the recipes
    # steps_set ([] --> list)

    def __str__(self):
        return self.name


class Steps( models.Model ):
    step_text = models.TextField(max_length=5012, null=False )
    recipe = models.ForeignKey( Recipes, on_delete=models.CASCADE, related_name='stepsForRecipe' )

class Ingredients( models.Model ):
    text = models.TextField( null=False )
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredientsForRecipe')