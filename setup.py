from setuptools import setup

setup(
    name='graphcommons',
    version='1.0.2',
    py_modules=['graphcommons'],
    url='https://github.com/graphcommons/graphcommons-python',
    license='MIT',
    author='Javier Fumanal',
    author_email='javier.fumanal@unavarra.es',
    description='Python Wrapper For Graph Commons API.',
    install_requires=['requests==2.5.3'],
)
