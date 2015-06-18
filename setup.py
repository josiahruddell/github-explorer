from setuptools import setup

setup(
    name='josiah.github.explorer',
    version='1',
    author='Josiah Ruddell',
    install_requires=[
        'flask>=0.10.1',
        'flask-restful>=0.3.1',
        'flask-testing',
        'nose',
        'requests'
    ]
)