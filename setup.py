from setuptools import setup, find_packages

setup(
    name = 'django-simplesearch',
    version = '0.1',
    description = 'A basic search application for Django.',
    long_description = open('README.md').read(),
    url = 'https://github.com/pigmonkey/django-simplesearch',
    author = 'Pig Monkey',
    author_email = 'pm@pig-monkey.com',

    packages = find_packages(),
    zip_safe=False,
)
