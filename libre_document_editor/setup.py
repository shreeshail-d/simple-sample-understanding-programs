import setuptools

setuptools.setup(
    name="cere_libre_tracker",
    version="1.0.0",
    author="Shreeshail D.",
    author_email="shreeshail.devmane.cerelabs@gmail.com",
    description="Libre changes tracker",
    long_description="A utility class to modify ODT documents by adding, deleting, or replacing text. Uses the odfpy library to manipulate OpenDocument Text (ODT) files.",
    long_description_content_type="text/markdown",
    url="www.cerelabs.com",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    include_package_data=True,
    install_requires=[
        "new_dtect_logging>=1.0.0",
        "cognitive_framework_commons>=5.1.0",
        "odfpy>=1.4.1"
    ],
)
