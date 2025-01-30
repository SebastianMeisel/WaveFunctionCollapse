from setuptools import setup, find_packages

setup(
    name="WaveFunctionCollaps",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    install_requires=[],
    author="sebastian.meisel+wfc@gmail.com",
    description="Implement wave function collapse algorithm.",
    python_requires=">=3.11"
)

# Local Variables:
# jinx-languages: "en_US"
# End:
