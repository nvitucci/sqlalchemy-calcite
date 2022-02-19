import os

from setuptools import find_packages
from setuptools import setup

readme = os.path.join(os.path.dirname(__file__), "README.md")

setup(
    name="sqlalchemy_calcite",
    version="0.0.1",
    description="Apache Calcite Dialect for SQLAlchemy and Apache Superset",
    long_description=open(readme).read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Database :: Front-Ends",
        "Operating System :: OS Independent",
    ],
    install_requires=["sqlalchemy", "jpype1"],
    extras_require={"dev": ["black", "flake8"]},
    keywords="Apache Calcite Superset SQLAlchemy dialect",
    author="Nicola Vitucci",
    author_email="nicola.vitucci@gmail.com",
    url="https://github.com/nvitucci/sqlalchemy-calcite",
    license="Apache",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "sqlalchemy.dialects": [
            "calcite = sqlalchemy_calcite.jdbc:CalciteDialectJdbc",
            "calcite.jdbc = sqlalchemy_calcite.jdbc:CalciteDialectJdbc",
        ]
    },
)
