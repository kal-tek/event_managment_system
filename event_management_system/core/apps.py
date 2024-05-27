from django.apps import AppConfig


class CoreConfig(AppConfig):
    """CoreConfig class to configure the core app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "event_management_system.core"

    def ready(self) -> None:
        """
        Set up the app.

        - Imports views and typing so we can use core.views and core.typing in urls.py.
        - Let django-stubs-ext monkeypatch some classes to add generic type support.
        """
        import django_stubs_ext
        from rest_framework import fields, generics

        django_stubs_ext.monkeypatch(
            extra_classes=(
                fields.Field,
                generics.GenericAPIView,
            ),
        )

        # pylint: disable=unused-import
        # ruff: noqa: F401
        from . import typing, views
