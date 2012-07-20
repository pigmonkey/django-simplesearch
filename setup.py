from setuptools import setup, find_packages

setup(
    name = 'django-simplesearch',
    packages = find_packages(),
    version = '1.0',
    description = 'A basic search application for Django.',
    author = 'Julien Phalip, Peter Hogg',
    author_email = 'peter@havenaut.net',
    url = 'https://github.com/pigmonkey/django-simplesearch',
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
    ],
    long_description = open('README.md').read(),
    include_package_data = True,
    zip_safe=True,
)
