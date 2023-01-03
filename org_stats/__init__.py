from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bg-stats")
except PackageNotFoundError:
    # package is not installed
    pass
