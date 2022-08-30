from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "src.{{ cookiecutter.project_slug }}"
    verbose_name = _("{{ cookiecutter.project_name }}")
