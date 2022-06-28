from django.contrib import admin
from django.contrib.auth.models import Group, User

# admin.site.unregister(User)
# admin.site.unregister(Group)

admin.site.site_header = 'Django F André Login'
admin.site.site_title = 'Administração DjangoFA'
admin.site.index_title = 'Administração DjangoFA - Aplicações'
