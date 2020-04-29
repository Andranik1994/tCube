import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='tCube',
     version='0.1',
     scripts=['tCube'] ,
     author="Andranik Alajajyan",
     author_email="andranik.alajajyan@gmail.com",
     description="Automated Unit Test Generator",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Andranik1994/tCube",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )