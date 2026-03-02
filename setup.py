from setuptools import setup, find_packages

setup(
    name='akatoollite_env',
    version='0.0.1',
    description='akatool lite enviroment',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/edprompt_env',
    packages=find_packages(exclude=[]),
    install_requires=['akatoollite', 'edprompt_env', 'cython', 'cffi', 'pyximport'],
    keywords=['python', 'shell', 'prompt', 'cli', 'editer', 'joke' 'saver', 'edprompt', 'env', 'edpromptenv', 'edprompt_env'],
    python_requires='>=3.13',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)
