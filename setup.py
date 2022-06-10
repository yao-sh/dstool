import setuptools

long_description = ""

setuptools.setup(
    name="dstool",
    version="0.0.1",
    author="Xiaozhe Yao",
    author_email="askxzyao@gmail.com",
    description="Toolkit for Data Scientists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dstool.yao.sh",
    packages=['dstool'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    install_requires=[
        "requests",
        "loguru"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/yao-sh/dstool/issues",
        "Documentation": "https://dstool.yao.sh/",
        "Source Code": "https://github.com/yao-sh/dstool",
    },
)