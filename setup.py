import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="apoor",
    version="1.1.1",
    author="Austin Poor",
    author_email="a-poor@users.noreply.github.com",
    description="A small personal package written in Python with reusable code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/apoor",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    install_requires=[
        "numpy"
        "pandas",
      ],
    python_requires=">=3.6",
    zip_safe=False
)
