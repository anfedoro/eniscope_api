from setuptools import setup, find_packages

setup(
    name='your_package_name',  # package name
    version='0.3',  # package version
    packages=find_packages(),  # auto find all packages
    install_requires=[  # package dependencies
        'requests>=2.31.0',  # for example
        'cryptography==41.0.3'
        'keyring==24.2.0'
    ],
    author='anfedoro',  # author name or organization
    author_email='andrei.fedorov@refactorenergy.es',  # email address
    description='Clien API linrary to access Eniscope (Best Energy) analytic database',  #short description
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',  # Type of the long description
    url='https://github.com/anfedoro/eniscope',  # Url to the github repo
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status
        'Intended Audience :: Developers',  # Audience
        'Programming Language :: Python :: 3.11',
        
    ],
    keywords='eniscope, energy, monitoring, analytic, api',  # keywords
    python_requires='>=3.11',  # minimum python version required
)
