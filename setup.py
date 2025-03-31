import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KK_Pairip",
    version="2.2",
    author="KK_Modstool",
    author_email="Modstool1@gmail.com",
    description="Recover String & Rebuild Apk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/Modstool/KK_Pairip",
    keywords='KKPairip',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13.5',
    entry_points={
        'console_scripts': [
            'KKPairip=KKPairip.__main__:KK_Modstool',
        ],
    },
)
