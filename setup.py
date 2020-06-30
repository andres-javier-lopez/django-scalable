import setuptools


setuptools.setup(
    name='bookstore',
    version='0.1.1',
    author='Andres Javier Lopez',
    author_email='ajavier.lopez@gmail.com',
    description='A sample bookstore project',
    packages=setuptools.find_packages(),
    scripts=['manage.py'],
)
