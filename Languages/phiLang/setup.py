from setuptools import setup, find_packages

setup(
    name="philang",
    version="1.0.0",
    description="ΦLang - Mathematical Programming Language",
    author="Lichen Collective",
    author_email="lmc.theory@gmail.com",
    packages=find_packages(),
    install_requires=["numpy>=1.21.0"],
    entry_points={
        'console_scripts': [
            'philang=src.cli:main',
        ],
    },
    python_requires=">=3.8",
)
