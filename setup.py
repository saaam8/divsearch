from setuptools import setup, find_packages

setup(
    name='divsearch',
    version='1.1.0',
    description='Adaptive Divisional Search Algorithm for high-dimensional data',
    author='Sattam',
    author_email='you@example.com',
    url='https://github.com/saaam8/ADS-Search',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
