from setuptools import setup

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read();

setup(
    name = "rds-host",
    version = "0.1.2",
    author = "Neil Kandalgaonkar",
    author_email = "neilk@neilk.net",
    description = "Get hostname from Amazon RDS instance name",
    long_description = readme,
    license = "MIT",
    url = "https://github.com/neilk/rds-host",
    download_url="https://github.com/neilk/rds-host/archive/v0.1.2.tar.gz",
    keywords = ["amazon", "aws", "psql", "cloud", "boto", "rds"],
    install_requires = ['boto>=2.2'],
    scripts = ["bin/rds-host", "bin/rds-psql"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
        ],
)
