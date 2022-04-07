import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='idf-to-ifc-pkg',
    version='0.0.1',
    author='Angel Diaz',
    author_email='angeldiaz017@hotmail.com',
    description='Python package for IDF to IFC file format transformation (Encore Project)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/angeldiaz017/IDFtoIFC',
    license='MIT',
    packages=['idf-to-ifc-pkg'],
    install_requires=['requests'],
)