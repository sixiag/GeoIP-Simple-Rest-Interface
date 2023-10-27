"""
Setup file for GeoIP
"""
from setuptools import setup, find_packages


__project__ = "GeoIP"


setup(
    name=__project__,
    version="1.0",
    description="Geolocation look up tool",
    packages=find_packages(include=("GeoIP", "GeoIP.*")),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": "geoip=GeoIP.iplookup:main"
    }
)
