from django.contrib.auth.middleware import (
    RemoteUserMiddleware as dj_RemoteUserMiddleware,
)
from rest_framework import permissions
import os


class ObjectPermissions(permissions.DjangoObjectPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": ["%(app_label)s.view_%(model_name)s"],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


class RemoteUserMiddleware(dj_RemoteUserMiddleware):
    header = os.environ.get("REMOTE_USER_HEADER_NAME", "HTTP_REMOTE_USER")
