"""
geometry_analysis
A python package for the MolSSI Software Summer School 2019.
"""

# Add imports here
from .molecule import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
