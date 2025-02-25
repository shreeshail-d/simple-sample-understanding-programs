import setuptools

with open("README.md", "r") as fh:
    lstr_long_description = fh.read()

setuptools.setup(
    name="Calculator",
    version="1.0.0",
    description='Simple Computer',
    author='Shreeshail D',
    author_email='shreeshail.devmane.cerelabs@gmail.com',
    long_description=lstr_long_description,
    long_description_content_type="text/markdown",
    url="www.cerelabs.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=['cognitive-framework-commons>=5.0.4',
                      'new_dtect_logging>=1.0.0', ]
)
