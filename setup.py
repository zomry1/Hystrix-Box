from distutils.core import setup

with open('README.md', 'r') as fh:
	long_description = fh.read()

setup(
  name = 'Hystrix-Box',         # How you named your package folder (MyLib)
  packages = ['Hystrix-Box'],   # Chose the same as "name"
  version = Hystrix-Box.__version__ ,      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Ultimate toolbox for solving CTF challenges',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'zomry1',                   # Type in your name
  author_email = 'zomry1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/zomry1/Hystrix-Box/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/zomry1/Hystrix-Box/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['CTF', 'toolbox', 'challenges'],   # Keywords that define your package best
  packages=setuptools.find_packages(),
  scripts=['menu.py']
  install_requires=[            # I get to this in a second
    'requests', 'Pillow', 'console_menu '
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)