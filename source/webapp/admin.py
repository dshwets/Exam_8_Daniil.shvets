from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Profile
from webapp.models import Product, Review
from django.contrib.auth.admin import UserAdmin

admin.site.register(Product)
admin.site.register(Review)
# admin.site.register(Issues)


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ['about', 'github_account', 'avatar']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


User = get_user_model()
admin.site.unregister(User)

admin.site.register(User, ProfileAdmin)
# admin.site.register(Project)
