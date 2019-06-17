from os import path
from setuptools import setup, find_packages


setup(
    name='wtlogger',
    version='0.0.2',

    description='Work Time Logger.',
    long_description='Work Time Logger.',

    url='https://pkonarzewski.github.com',

    author='PKonarzewski',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='time logger work',
    packages=find_packages(exclude=['tests']),
    install_requires=['alembic>=1.0,<1.1',
                      'pandas>=0.24,<0.25',
                      'sqlalchemy>=1.3,<1.4',
                      'Click==7.0'
                      ],
    entry_points={
        'console_scripts': [
            'wtl=wtlogger.cli:main',
        ],
    },

    # $ pip install -e .[dev]
    extras_require={
        'dev': ['pylint', 'mypy', 'tox']
    },
    python_requires='~=3.6'
)
