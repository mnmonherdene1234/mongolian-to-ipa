import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="mongolian2ipa", version="0.0.3", author="mnmonherdene",
                 author_email="mnmonherdene1234@gmail.com",
                 description="Mongolian text to International Phonetic Alphabet", long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/mnmonherdene1234/mongolian-to-ipa", packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent", ], )
