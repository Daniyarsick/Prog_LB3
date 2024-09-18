from setuptools import setup, find_packages

setup(
    name='myweather',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'myweather=myweather.getweatherdata:main',
        ],
    },
    author='Daniil Annanurov',
    author_email='dan.annanurov@gmail.com',
    description='A simple weather data fetching package using OpenWeather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/daniyarsick',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)