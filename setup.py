import setuptools


VERSION = '0.1.6'


setuptools.setup(
    name='pynote',
    packages=setuptools.find_packages(),
    version=VERSION,
    description='Note taking app.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Euromance/pynote',
    author='Euromance',
    author_email='kysput@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    project_urls={
        'Repository': 'https://github.com/Euromance/pynote',
    },
    python_requires='>=3.9,<4',
    install_requires=[
        'confboy>=0.2.0,<1.0.0',
        'typer[all]>=0.3.0,<1.0.0',
    ],
    extras_require={
        'dev': [
            'flake8-commas==2.0.0',
            'flake8-import-order==0.18.1',
            'flake8-quotes==3.2.0',
            'flake8==3.9.1',
            'pep8-naming==0.11.1',
        ],
        'test': [
            'pytest-cov==2.11.1',
            'pytest-mock==3.5.1',
            'pytest==6.2.2',
        ],
    },
    entry_points={
        'console_scripts': [
            'note=pynote:app',
        ],
    },
)
