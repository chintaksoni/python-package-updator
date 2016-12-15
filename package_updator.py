__author__ = "Chintak"

import pip
import requests
import json
from version_comparator import compare_version


base_url = "https://pypi.python.org/pypi/"

installed_packages = pip.get_installed_distributions()
for package in installed_packages:
	pkg = str(package)
	name, current_version = pkg.split(' ')

	url = base_url + name +"/json"
	req = requests.get(url)
	pkg_data = json.loads(req.text)

	# Get lattest version of package
	latest_version = pkg_data['info']['version']

	is_new_version = compare_version(current_version, latest_version)
	if is_new_version:
		print "Package : %s ,version needs to be updated."%(name)

	else:
		print "Package : %s ,version is up-to-date."%(name)