from django.contrib import admin

# Register your models here.
from .models import (
    ACL,
    Device,
    Equipment,
    Location,
    LocationCategory,
    Notification,
    NotificationCategory,
    Operation,
    Organization,
    Person,
    PersonProperty,
    PersonPropertyGroup,
    Project,
    Resource,
    Role,
    RoleSpecification,
    Shift,
    Task,
    TaskField,
)

admin.site.register(ACL)
admin.site.register(Device)
admin.site.register(Equipment)
admin.site.register(Location)
admin.site.register(LocationCategory)
admin.site.register(Notification)
admin.site.register(NotificationCategory)
admin.site.register(Operation)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(PersonProperty)
admin.site.register(PersonPropertyGroup)
admin.site.register(Project)
admin.site.register(Resource)
admin.site.register(Role)
admin.site.register(RoleSpecification)
admin.site.register(Shift)
admin.site.register(Task)
admin.site.register(TaskField)
