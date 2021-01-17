import setuptools

with open("README.md") as f:
    long_description = f.read()

# from sphinx.setup_command import BuildDoc
# cmdclass = {'build_sphinx': BuildDoc}

name = 'apoor'
version = "1.2.0"
release = version

setuptools.setup(
    name=name,
    version=version,
    author="Austin Poor",
    author_email="a-poor@users.noreply.github.com",
    description="A small personal package created to store code and data I often reuse.",
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
        "Development Status :: 5 - Production/Stable",
    ],
    install_requires=[
        "numpy",
        "pandas",
      ],
    python_requires=">=3.6",
    zip_safe=False,
    # command_options={
    #     'build_sphinx': {
    #         'project': ('setup.py', name),
    #         'version': ('setup.py', version),
    #         'release': ('setup.py', release),
    #         'source_dir': ('setup.py', 'doc')}},
)


