VERSION = (0, 2, 0, 'dev')


def get_version():
    return '.'.join(str(v) for v in VERSION)
