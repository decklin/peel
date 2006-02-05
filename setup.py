#!/usr/bin/env python

from distutils.core import setup

setup(
    name='lastfmsubmitd',
    version='0.9',
    description='Last.fm submit daemon and example clients for MPD/MusicBrainz',
    author='Decklin Foster',
    author_email='decklin@red-bean.com',
    url='http://www.red-bean.com/~decklin/software/lastfmsubmitd/',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 4 - Beta',
        'License :: MIT/X Consortium License',
        'Topic :: Multimedia :: Sound :: Players',
        'Operating System :: POSIX',
        'Environment :: No Input/Output (Daemon)',
        'Programming Language :: Python',
        ],
    package_dir = {'': 'lib'},
    packages = ['lastfm'],
    scripts = [
        'lastfmsubmitd',
        'lastfmsubmit',
        'lastmp',
        'lastcd',
        'mbfind',
        'mbget',
        'mbsubmit',
        ],
    data_files=[
        # ('share/man1', ['lastfmsubmitd.1', 'etc...']),
        ],
    )
