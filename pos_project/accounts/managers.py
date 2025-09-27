from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

class UserManager(BaseUserManager):
    def create_user(self, username, email, full_name, mobile, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        if not username:
            raise ValueError('El username es obligatorio')
            
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            full_name=full_name,
            mobile=mobile,
            **extra_fields
        )
        
        if password:
            user.set_password(password)
        else:
            # Generar contraseña aleatoria
            password = User.objects.make_random_password(
                length=8,
                allowed_chars="abcdefghjkmnpqrstuvwxyz0123456789"
            )
            user.set_password(password)
            
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, full_name=None, mobile=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')
            
        return self.create_user(
            username=username,
            email=email, 
            full_name=full_name or username,
            mobile=mobile or '000000000',
            password=password,
            **extra_fields
        )