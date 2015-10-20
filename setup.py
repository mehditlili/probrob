#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(### Metadata ###.
      name='probrob',
      version='0.2',
      author='Chris Murphy',
      author_email='chrismurf@whoi.edu',
      description='Python Probabilistic Robotics',
      long_description="""This project contains Python implementations of
various probabilistic robotics techniques, including (but not limited to) the
Particle Filter, Kalman Filter, Extended Kalman Filter, and Rao-Blackwellized
Particle Filter. It also has utilities for plotting simulations.""",
      license='MIT',
      url='https://launchpad.net/probrob',

      ### Packaging ###
      packages     = ['probrob'],
      #scripts = ['scripts/XX']
)
