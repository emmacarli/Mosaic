from setuptools import setup

setup(name='mosaic',
      version='0.1',
      description='Code for generating point spread functions and beam tiling for radio interferometers',
      url='https://gitlab.mpifr-bonn.mpg.de/wchen/Beamforming/',
      author='Weiwei Chen',
      author_email='wchen@mpifr-bonn.mpg.de',
      license='MIT',
      packages=['mosaic'],
      install_requires=[
          'scipy == 1.2.2',
          'numpy == 1.16',
          'matplotlib == 2.2.3',
          'katpoint',
          'nvector',
          'astropy == 2.0.7'
      ],
      zip_safe=False)
