from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='segmind',
      version='0.2.2',
      description='Package for Using Segmind APIs in Python',
      url='https://docs.segmind.com/apis',
      author='Yatharth Gupta',
      license='MIT',
      packages=['segmind'],
      author_email='yatharthg@segmind.com',
      install_requires=[
          'pillow',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)