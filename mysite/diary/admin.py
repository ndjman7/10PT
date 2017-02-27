from django.contrib import admin
from .models import FutureDiary, RealDiary


class FutureDiaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'content')


class RealDiaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'content')


admin.site.register(FutureDiary, FutureDiaryAdmin)
admin.site.register(RealDiary, RealDiaryAdmin)
