from django.contrib import admin

from users.models import Client, Freelancer, User

# Register your models here.
admin.site.register(User)
admin.site.register(Freelancer)
admin.site.register(Client)
