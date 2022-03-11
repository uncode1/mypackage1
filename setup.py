from setuptools import setup, find_packages

setup(
    name='mypackage1',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/uncode1/mypackage1',
    author='SUMANU, Peter.',
    author_email='petersumanu@yahoo.com'
)
