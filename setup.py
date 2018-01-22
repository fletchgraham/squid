from setuptools import setup

setup(
    name='squid',
    version='1.0',
    packages=['squid'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        squid=squid.main:squid
    ''',
)
