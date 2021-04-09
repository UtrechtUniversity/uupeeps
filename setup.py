import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uupeeps",
    version="0.0.1",
    author="Class CoTaPP",
    author_email="j.debruin1@uu.nl",
    description="Utrecht University employee info scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UtrechtUniversity/uupeeps",
    project_urls={
        "Bug Tracker": "https://github.com/UtrechtUniversity/uupeeps/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
