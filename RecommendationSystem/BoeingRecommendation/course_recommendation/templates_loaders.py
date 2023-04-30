import os
from django.template.loaders.filesystem import Loader as FilesystemLoader

class PackageLoader(FilesystemLoader):
    def get_template_sources(self, template_name):
        app_name = 'course_recommendation'
        app_module = __import__(app_name)

        template_dir = os.path.join(os.path.dirname(app_module.__file__), 'templates')
        return super().get_template_sources(template_name, template_dir=template_dir)
