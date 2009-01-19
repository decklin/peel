#!/usr/bin/python

from distutils.core import setup

setup(
    name='ears',
    version='1.0.1',
    description='MusicBrainz querying, CD-ripping, and Last.fm tools',
    author='Decklin Foster',
    author_email='decklin@red-bean.com',
    url='http://www.red-bean.com/decklin/ears/',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 4 - Beta',
        'License :: MIT/X Consortium License',
        'Topic :: Multimedia :: Sound :: Players',
        'Operating System :: POSIX',
        'Environment :: Console (Text Based)',
        'Programming Language :: Python',
        ],
    scripts = [
        'lastcd',
        'mbfind',
        'mbget',
        'mbsubmit',
        'peel',
        ],
    data_files=[
        ('share/man/man1', [
            'doc/mbget.1',
            'doc/peel.1',
            ]),
        ],
    )
