from setuptools import setup, find_packages

setup(
    name="ccr",
    version="0.0.1",
    author="Conor J. Wild",
    author_email="conorwild@gmail.com",
    description="Correlation Constrained Regression",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
    ],
)
