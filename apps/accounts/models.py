from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    cell_phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis do usuários'
    
    def __str__(self):
        return self.user.username