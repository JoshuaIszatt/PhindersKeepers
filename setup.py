from setuptools import find_packages, setup

setup(
    name="PhindersKeepers",
    version="0.0.1",
    description="Python package designed to easily subset inphared data",
    url="https://github.com/JoshuaIszatt",
    author="Joshua Iszatt",
    author_email="joshiszatt@gmail.com",
    license="AGPL-3.0",
    install_requires=["pandas >= 1.5.3", "biopython >= 1.79"],
    python_requires=">3",
    packages=find_packages(),
    data_files=[("", ["LICENSE.md", "README.md"])],
    entry_points={
        'console_scripts': [
            'phinders_keepers.py = PhindersKeepers.main:main',
        ],
    },
)