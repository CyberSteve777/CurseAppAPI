from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Cuseforge App API"
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="curse_app_api",
    version=VERSION,
    author="CyberSteve777",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
        'selenium',

    ],
    python_requires=">=3.6",
    keywords=['python', 'minecraft', 'curseforge'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows",
    ]
)
