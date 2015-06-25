from setuptools import setup, find_packages

from django_chart_js import VERSION

with open('README.rst') as f:
    readme = f.read()

setup(
    name='django_chart_js',
    version='.'.join(map(str, VERSION)),
    description='Django Chart.js wrapper',
    author='deliro',
    author_email='t4k.kitaetz@gmail.com',
    long_description=readme,
    license='Apache 2.0',
    requires=['django'],
    packages=find_packages(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),
)
