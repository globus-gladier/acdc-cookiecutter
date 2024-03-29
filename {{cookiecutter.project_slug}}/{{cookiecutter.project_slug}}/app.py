
from django.apps import AppConfig
from {{cookiecutter.project_slug}} import checks

class {{cookiecutter.project_slug.capitalize().replace("_", "")}}(AppConfig):
    name = '{{cookiecutter.project_name}}'



SEARCH_INDEXES = {
    "{{cookiecutter.project_slug}}": {
        "uuid": "{{cookiecutter.search_index_uuid}}",
        "name": "{{cookiecutter.project_name}}",
        "template_override_dir": "{{cookiecutter.project_slug}}",
        "fields": [],
    }
}