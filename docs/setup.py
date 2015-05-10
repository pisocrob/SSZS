try:
	from setuptools import setup
except ImportError:

config = {
	'description': 'SS:ZS',
	'author':'PiSocRob',
	'url': 'https://github.com/pisocrob',
	'download_url': 'https://github.com/pisocrob/SSZS',
	'author_email': 'Pending',
	'version': 'a0.1',
	'install_requires': ['nose'],
	'packages': ['SSZS'],
	'scripts': [],
	'name': 'SS:ZS'
}

setup(**config)