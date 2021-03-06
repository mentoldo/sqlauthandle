#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0',
                'sqlalchemy',
                'configparser',
                'keyring',
                'Path',
                'tk']

test_requirements = ['pytest>=3', ]

setup(
    author="Matías Adrián Alfonso",
    author_email='matias.alfonso@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Easy manage Authentication on SQL DB.",
    entry_points={
        'console_scripts': [
            'sqlauthandle=sqlauthandle.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sqlauthandle',
    name='sqlauthandle',
    packages=find_packages(include=['sqlauthandle', 'sqlauthandle.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mentoldo/sqlauthandle',
    version='0.1.1',
    zip_safe=False,
)
