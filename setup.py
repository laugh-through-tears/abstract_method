from setuptools import setup, find_namespace_packages

setup(
    name='personal-assistant-bot',
    version='0.2.8',
    license='MIT License',
    url='https://github.com/avtarso/python_core_21_team_11_project/',
    author='Avtarso',
    author_email='t0676352927@gmail.com',
    description='Command line personal assistant bot',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['colorama'],
    entry_points={
        'console_scripts': ['pab = personal_assistant_bot.main:main'],
    },
)
