import os.path as _path


def root(*paths):
    return _path.join(_path.dirname(_path.dirname(_path.dirname(_path.abspath(__file__)))), *paths)


def assets(*paths):
    return root('assets', *paths)


def output(*paths):
    return root('output', *paths)
