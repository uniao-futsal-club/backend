from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from .fields import PasswordField, UpperCaseField, IntegerRangeField


# Register your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email,
                          password=password, ** extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    ROLE_CHOICES = (
        (1, 'coach'),
        (2, 'player'),
    )
    asset = models.ForeignKey('asset.Asset', verbose_name='Foto de Perfil',
                              on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=60,
                              unique=True, null=False, blank=False)
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True, null=False, blank=False)
    first_name = UpperCaseField(
        'Nome', max_length=30, null=False, blank=False)
    last_name = UpperCaseField(
        'Sobrenome', max_length=60, null=False, blank=False)
    birthday = models.DateField(
        'Data de Nascimento', auto_now=False, auto_now_add=False)
    role = models.PositiveSmallIntegerField(
        'Papel de Usuário', choices=ROLE_CHOICES, null=False, blank=False)
    created = models.DateTimeField('Data de Entrada', auto_now_add=True)
    password = PasswordField('Senha', max_length=128, null=False, blank=False)
    is_staff = models.BooleanField('Equipe', default=False)  # django user
    is_active = models.BooleanField('Ativo', default=True)  # django user

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birthday']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class Coach(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Técnico"
        verbose_name_plural = "Técnicos"


class Player(models.Model):
    POSITION_CHOICES = (
        (1, 'goalkeeper'),
        (2, 'fixed'),
        (3, 'wing'),
        (4, 'pivot'),
    )
    UNIFORM_SIZE_CHOICES = (
        (1, 'PP'),
        (2, 'P'),
        (3, 'M'),
        (4, 'G'),
        (5, 'GG'),
    )
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    number = models.PositiveIntegerField("Número", null=False)
    position = models.PositiveSmallIntegerField(
        'Posição em Quadra', choices=POSITION_CHOICES, null=False, blank=False)
    height = models.DecimalField(
        "Altura em metros", max_digits=5, decimal_places=2)
    weight = models.DecimalField(
        "Peso em quilogramas", max_digits=5, decimal_places=2)
    age = models.PositiveSmallIntegerField(
        "Idade em anos", null=False, blank=False)
    uniform_size = models.PositiveSmallIntegerField(
        'Tamanho do Uniforme', choices=UNIFORM_SIZE_CHOICES, null=False, blank=False)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"


class Skills(models.Model):
    player = models.ForeignKey(
        "accounts.Player", verbose_name="Jogador", on_delete=models.CASCADE)
    goalkeeper = IntegerRangeField(
        min_value=1, max_value=99, null=False, default=50)
    fixed = IntegerRangeField(
        min_value=1, max_value=99, null=False, default=50)
    wing = IntegerRangeField(min_value=1, max_value=99, null=False, default=50)
    pivot = IntegerRangeField(
        min_value=1, max_value=99, null=False, default=50)
    created_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
