from django.contrib import admin

from .user import UserModelAdmin

admin.site.site_header = "Event Management System Admin"
admin.site.site_title = "Event Management System Admin"
admin.site.index_title = "Welcome to the Even tManagement System Admin"

__all__ = ("UserModelAdmin",)
