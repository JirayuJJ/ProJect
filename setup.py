from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='ProJect',
    version='0.1',
    description='Grandma Somsri and Grandpa Prayud',
    long_description=readme(),
    url='https://github.com/JirayuJJ/ProJect',
    author='SomsriCat',
    author_email='your_email@example.com',
    license='Somsri',
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    scripts=['bin/ProJect-status',
             'bin/grandpaprayud-status',
             'bin/graph-power'],
    keywords='ProJect grandpaprayud somsri prayud',
    packages=['ProJect'],
    package_dir={'ProJect': 'src/ProJect'},
    package_data={'ProJect': ['graph/*.py']
    },
)
