try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Xu Yi',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'xuyi@ziad.cn',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
