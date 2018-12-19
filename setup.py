from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file_stream:
    long_description = readme_file_stream.read()

setup(
    name='ig-streaming-client',
    version='0.1',
    description='IG streaming API client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wjszlachta/ig-streaming-client',
    author='Wojciech Szlachta',
    author_email='wojciech@szlachta.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3'
    ],
    keywords='IG trading',
    project_urls={
        'Bug Reports': 'https://github.com/wjszlachta/ig-streaming-client/issues',
        'Source': 'https://github.com/wjszlachta/ig-streaming-client'
    },

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['ig-rest-client',
                      'lightstreamer-client'],

    include_package_data=True
)
