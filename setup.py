try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Git Dashboard',
    description='A small git deploy dashboard',
    author='Paul Traylor',
    url='http://github.com/kfdm/git-dash/',
    version='0.0.1',
    packages=['gitdash'],
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'git-dash = gitdash.cli:main'
        ]
    }
)
