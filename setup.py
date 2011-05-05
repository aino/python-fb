from setuptools import setup, find_packages


setup(
    name='python-fb',
    version='0.1',
    description='This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, which is the canonical way to implement Facebook authentication.',
    long_description=open('README.md').read(),
    author='Mikko Hellsing',
    author_email='mikko@aino.se',
    url='https://github.com/aino/python-fb',
    packages=find_packages(),
    zip_safe=False,
)
