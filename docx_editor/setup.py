import setuptools

setuptools.setup(
    name="cere_doc_editor",
    version="1.0.0",
    author="Shreeshail D.",
    author_email="shreeshail.devmane.cerelabs@gmail.com",
    description="Cere Document Editor",
    long_description="CereDocEditor is a Python class designed to manipulate and edit `.docx` documents using the `python-docx` library. It provides functionalities such as opening a document, adding statements, deleting text, replacing text, and saving the document.",
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
        "python-docx>=1.1.2"
    ],
)
