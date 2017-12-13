from setuptools import setup

setup(
    name='fb-down',
    version='1.0.1',

    description='FB Down is a simple FB Video Downloader',
    long_description="visit https://tbhaxor.github.io/fbdown",
    url='https://tbhaxor.github.io/fbdown',

    author='Gurkirat Singh',
    author_email='tbhaxor@gmail.com',

    license='GNU',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: GNU General Public License (GPL)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='gurkirat fbdown fb tbhaxor',

    packages=["fbdown"],
    install_requires=['tqdm', "argparse"],
    entry_points={
        'console_scripts': [
            'fbdown=fbdown:TheMain',
        ],
    },

)
