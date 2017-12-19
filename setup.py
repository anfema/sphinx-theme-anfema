# -*- coding: utf-8 -*-
"""
.. _github: https://github.com/anfema/sphinx-theme-anfema

"""
from setuptools import setup


setup(
    name='sphinx-theme-anfema',
    version='0.3.1',
    url='https://github.com/anfema/sphinx-theme-anfema',
    license='BSD',
    author='Johannes Schriewer',
    author_email='hallo@dunkelstern.de',
    description='anfema theme for Sphinx.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['sphinx-theme-anfema', 'swift_domain'],
    package_data={
        'sphinx-theme-anfema': [
            'theme.conf',
            '*.html',
            'static/css/*.css'
        ]
    },
    entry_points={
        'console_scripts': [
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    install_requires=[
        'fuzzywuzzy',
        'sphinx'
    ]
)
