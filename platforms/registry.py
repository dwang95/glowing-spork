
from platforms import local


registered_platforms = {'local': local.Platform}


def get(name):
    return registered_platforms[name]
