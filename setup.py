"""Install package."""

import setuptools

setuptools.setup(
    name="OctoPrint-PSUControl-Meross",
    version="0.0.1",
    description="Adds Meross Smart Plug support to OctoPrint-PSUControl",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[],
    license="License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    author="Ilja Orlovs",
    author_email="vrghost@gmail.com",
    url="https://github.com/VRGhost/OctoPrint-PSUControl-Meross",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    py_modules=[
        "octoprint_psucontrol_meross",
    ],
    entry_points={
        "octoprint.plugin": ["psucontrol_meross = octoprint_psucontrol_meross"]
    },
    python_requires=">=3.6",
)
