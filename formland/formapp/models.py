from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, real_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, real_name=real_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, real_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, real_name, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    real_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'real_name']

    # Add related_name to avoid clash with auth.User.groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    # Add related_name to avoid clash with auth.User.user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.email
from django.db import models
import uuid

class MachineModel(models.Model):
    username = models.CharField(max_length=30)  # Assuming a CharField for simplicity
    machine = models.CharField(max_length=100)
    machine_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pictures = models.ImageField(upload_to='machine_pics/')
    description = models.TextField()

    def __str__(self):
        return f"{self.machine} ({self.machine_id})"

class UserProfileModel(models.Model):
    username = models.CharField(max_length=30)  # Assuming a CharField for simplicity, you can use ForeignKey to link to a User model
    insta = models.CharField(max_length=50, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username}'s Profile"
