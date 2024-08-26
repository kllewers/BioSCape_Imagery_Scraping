from setuptools import setup, find_packages

setup(
    name='BioSCrapes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'requests'
    ],
    author='Kit Lewers',
    author_email='kristen.lewers@colorado.edu',
    description='Allows you to scrape all or specific files for BioSCape from JPL',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kllewers/BioSCrapes',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)