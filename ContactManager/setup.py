from setuptools import setup, find_packages

setup(
    name='ContactManager',
    version='0.1',
    license='Hamidreza Zamanian',
    author='Hamidreza Zamanian',
    author_email='hamid80zamanian@gmail.com',
    description='This is a command-line contact notebook program',
    keywords='contact',
    url='https://github.com/HamidrezaZMN/',
    project_urls={
        'source code' : 'https://github.com/HamidrezaZMN/ContactManager/'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        contact=program.contact:contact
    ''',
)