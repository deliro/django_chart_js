from django_chart_js import VERSION

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django_chart_js',
    version='.'.join(map(str, VERSION)),
    description='Django Chart.js wrapper',
    author='deliro',
    author_email='t4k.kitaetz@gmail.com',
    requires=['django'],
    packages=['django_chart_js'],
)
