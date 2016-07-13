#!/usr/bin/env python
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 23 Jun 20:22:28 2011 CEST
# vim: set fileencoding=utf-8 :

"""The db package contains simplified APIs to access data for various databases
that can be used in Biometry, Machine Learning or Pattern Classification."""

import pkg_resources

from . import utils, driver
from .file import File
from .database import Database, SQLiteDatabase
from .annotations import read_annotation_file
__version__ = pkg_resources.require(__name__)[0].version


def get_config():
  """Returns a string containing the configuration information.
  """
  import bob.extension
  return bob.extension.get_config(__name__)


# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
