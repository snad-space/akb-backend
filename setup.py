import os
import sys
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='akb',
	version='0.1.0',
	packages=['akb'],
	include_package_data=True,
	description='Anomaly knowledge base backend',
	url='https://github.com/snad-space/akb-backend',
	author='Matwey V. Kornilov',
	author_email='matwey.kornilov@gmail.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
	test_suite='runtests.runtests',
	install_requires=[
		'Django',
		'djangorestframework',
	]
)

