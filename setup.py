from distutils.core import setup
import setuptools
import HystrixBox

with open('README.md', 'r', encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name = 'Hystrix-Box',        
    packages = setuptools.find_packages(),  
    version = HystrixBox.__version__ ,    
    license='MIT',       
    description = 'Ultimate toolbox for solving CTF challenges',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'zomry1',                   
    author_email = 'zomry1@gmail.com',    
    url = 'https://github.com/zomry1/Hystrix-Box/', 
    download_url = 'https://github.com/zomry1/Hystrix-Box/archive/v0.1-alpha.tar.gz',   
    keywords = ['CTF', 'toolbox', 'challenges'],
    entry_points = {
        'console_scripts': ['Hystrix-Box=HystrixBox.menu:main']
    },
    install_requires=['requests', 'Pillow', 'console_menu '],
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ]
)