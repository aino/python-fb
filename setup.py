from setuptools import setup, find_packages


setup(
    name='facebook-python-sdk',
    version='0.1',
    description='This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, which is the canonical way to implement Facebook authentication.',
    long_description=open('README.md').read(),
    author='Facebook',
    url='https://github.com/aino/facebook-python-sdk',
    packages=find_packages(),
    zip_safe=False,
)
