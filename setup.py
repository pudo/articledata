import os
from setuptools import setup, find_packages

path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(path, "README.md"), "r") as f:
    readme = f.read()

setup(
    name="articledata",
    version="0.1.2",
    description="Utility library for trading article data.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="articles media news journalism",
    author="Friedrich Lindenberg, Heleen Emanuel",
    author_email="friedrich@pudo.org",
    url="http://github.com/pudo/articledata",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "examples", "test"]),
    namespace_packages=[],
    package_data={"": ["articledata/py.typed"]},
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=["languagecodes", "pydantic"],
    extras_require={
        "dev": ["mypy", "wheel", "twine", "pytest", "types-PyYAML"],
    },
    tests_require=[],
    entry_points={},
)
