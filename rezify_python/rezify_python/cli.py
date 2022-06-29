"""
Entrypoint for CLI.
"""
import click
from rez.config import config
from .create_package import create_package


@click.command()
@click.option(
    "--release",
    "-r",
    is_flag=True,
    help="Release to release path instead of local path",
)
@click.option(
    "--packages_path", "-p", help="Release to custom path, overrides --release"
)
@click.option(
    "--python_version",
    "-v",
    required=True,
    help="Release specific version (latest if not set)",
)
def cli(release, packages_path, python_version):
    if not packages_path:
        packages_path = (
            config.release_packages_path if release else config.local_packages_path
        )
    create_package(packages_path=packages_path, python_version=python_version)
