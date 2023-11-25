#!/usr/bin/python3

from setuptools import setup

setup(name='open-fprintd',
      version='0.6',
      py_modules = [],
      packages=['openfprintd'],
      scripts=[],
      data_files=[
          ('lib/open-fprintd/', ['dbus_service/open-fprintd', 'scripts/suspend.py', 'scripts/resume.py']),
      ]
)
