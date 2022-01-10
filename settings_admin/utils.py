import os
import re
from importlib import import_module

from django.conf import settings


def overwrite_settings(options):
    m = import_module(os.environ.get('DJANGO_SETTINGS_MODULE'))
    with open(m.__file__, 'r') as f:
        contents = f.read()
    for k, v in options.items():
        contents = re.sub(f'^{k}\s?=.+$', f'{k} = {repr(v)}', contents, re.MULTILINE)
        setattr(settings, k, v)
    with open(m.__file__, 'w') as f:
        f.write(contents)

