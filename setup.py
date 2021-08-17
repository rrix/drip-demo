#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='drip-demo',
      version='0.01',
      # Modules to import from other scripts:
      packages=find_packages(),
      # Executables
      scripts=["auth_agent.py", "data_controller.py"],
     )
