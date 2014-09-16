try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Trajectory clustering',
        'author': 'Kan Huang',
        'url': 'huangkan.wordpress.com',
        'author_email': 'huangkandiy@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['Trajectory'],
        'scripts': [],
        'name': 'sandia'
        }

setup(**config)
