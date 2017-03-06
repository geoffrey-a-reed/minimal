from setuptools import setup

setup(name='Minimal',
      version='0.1.0',
      description='A minimal Python package',
      author='Geoffrey A. Reed',
      author_email='geoffrey.a.reed@gmail.com',
      url='https://github.com/geoffrey-a-reed/minimal',
      license='MIT',
      install_requires=[],
      extras_require={
          'tests': ['pytest'],
      },
      packages=['minimal']) 