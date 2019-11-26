
#from setuptools import setup, find_packages, find_namespace_packages
from distutils.core import setup
import re

packages = [
    "libdyer",
    "libdyer.notify",
    "libdyer.tasks"
]
package_dirs = {}
for package in packages:
    package_dirs[package] = re.sub("\.", "/", package)



setup(
    name="libdyer",
    version="2019.4",
    #package_data={'dyer':['data/Makefile', 'data/*.xsl', 'data/*.sty']},
    scripts=['scripts/dyer'],
    packages=packages,
    package_dir=package_dirs
    #packages=["libdyer", "libdyer.notify"],
    #package_dir={
    #    "libdyer": "libdyer",
    #    "libdyer.notify": "libdyer/notify"
    #}

)
        
