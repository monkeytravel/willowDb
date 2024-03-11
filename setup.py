from distutils.core import setup
setup(
    name = 'willowDb',
    packages = ['willowDb'],
    version = '0.1.1',
    license='MIT',
    description = 'A document database as a python module',
    author = 'Cameron Perrier',
    author_email = 'dev@thegalacticgroup.com',
    url = 'https://github.com/monkeytravel/willowDb',
    download_url = 'https://github.com/monkeytravel/willowDb/archive/refs/tags/v0.1.tar.gz',
    keywords = ['db', 'documentDb', 'nosql'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Source": "https://github.com/monkeytravel/willowDb",
    },
)