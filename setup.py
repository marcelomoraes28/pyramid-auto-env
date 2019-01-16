from setuptools import setup

requires = [
    'pyramid>=1.5'
]
extras_require = {
    'test': [
        'pytest==3.8.0',
        'pytest-mock==1.10.0',
        'pytest-cov==2.5.1',
    ],
    'ci': [
        'python-coveralls==2.9.1',
    ]
}

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pyramid_auto_env',
    version='0.1.2',
    description='Pyramid Autoenv',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    author='Marcelo Moraes',
    author_email='marcelomoraesjr28@gmail.com',
    url='https://github.com/marcelomoraes28/pyramid-auto-env',
    keywords='autoenv pyramid',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
    install_requires=requires,
    packages=['pyramid_auto_env']
)
