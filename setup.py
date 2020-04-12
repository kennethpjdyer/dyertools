
#from setuptools import setup, find_packages, find_namespace_packages
from distutils.core import setup
import re

packages = [
    "libdyer",
    "libdyer.notify",
    "libdyer.tasks",
    "libdyer.build",
    "libdyer.meetup"
]
package_dirs = {}
for package in packages:
    package_dirs[package] = re.sub("\.", "/", package)

scripts = ['dyer', 'mup']
script_list = []
for i in scripts:
    script_list.append(f"scripts/{i}")


setup(
    name="libdyer",
    version="2019.4",
    #package_data={'dyer':['data/Makefile', 'data/*.xsl', 'data/*.sty']},
    scripts=script_list,
    packages=packages,
    package_dir=package_dirs
    #packages=["libdyer", "libdyer.notify"],
    #package_dir={
    #    "libdyer": "libdyer",
    #    "libdyer.notify": "libdyer/notify"
    #}

)
        
