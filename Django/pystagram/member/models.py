from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('올바른 이메일을 입력하세요.')

        user = self.model( # self.mode = User()
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)

        # user.password = password 라 하지 않는 이유?
        '''
        password는 기본적으로 해시화됨
        암호화 / 해시화
        암호화 : qwe123 -> 암호화 -> asdfgq -> 복호화 -> qwe123
        해시화 : qwe123 -> asdflsdk333 -> 일부다시암호화(asdf) / 나머지정보는 유실됨 -> 암호화반복 -> dgfdg -> 복호화 불가능
        장고에서는 SHA256 이란걸 사용
        '''

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True
    )
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    nickname = models.CharField('nickname', max_length=20, unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email' # 원래 기본은 user, 대신 email로 사용하기 위해 선언
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = f'{verbose_name} 목록'

    def get_full_name(self):
        return self.nickname

    def get_shot_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
