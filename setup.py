#############################################################################
#
#   Setup based on Labelme install script:
#   https://github.com/wkentaro/labelme
#
##############################################################################
import re
from setuptools import setup, find_packages


def get_version():
    filename = "zero_dce/__init__.py"
    with open(filename) as f:
        match = re.search(
            r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M
        )
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version


def get_install_requires():
    install_requires = [
        "torch>=2.0.0"
    ]

    return install_requires


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()
    try:
        # when this package is being released
        import github2pypi

        return github2pypi.replace_url(
            slug="leonelhs/Zero-DCE", content=long_description, branch="main"
        )
    except ImportError:
        # when this package is being installed
        return long_description


def main():
    setup(
        name='zero_dce',
        version=get_version(),
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        packages=find_packages(),
        url='https://github.com/leonelhs/Zero-DCE',
        license='Apache',
        author='leonel hernandez',
        author_email='leonelhs@gmail.com',
        description='Zero-Reference Deep Curve Estimation for Low-Light Image Enhancement',
        install_requires=get_install_requires(),
        package_data={"zero_dce": []},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3 :: Only",
        ],
    )


if __name__ == "__main__":
    main()
