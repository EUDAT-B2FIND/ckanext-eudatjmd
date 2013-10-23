from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
	name='ckanext-eudatjmd',
	version=version,
	description="CKAN extension for eudat-jmd",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='EUDAT metadata task force',
	author_email='eudat-tf-metadata@postit.csc.fi',
	url='https://confluence.csc.fi/display/Eudat/Metadata+Task+Force',
	license='Public domain',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.eudatjmd'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.eudatjmd:PluginClass
        eudatjmd=ckanext.eudatjmd.plugin:EudatJmdPlugin
	""",
)
