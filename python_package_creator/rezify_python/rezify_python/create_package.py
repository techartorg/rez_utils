import os
import shutil
import logging
import subprocess
import urllib.request
import tempfile
import distutils.dir_util
from rez.package_maker import make_package

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def create_package(packages_path, python_version):
    """Release a python nuget package as rez package.
    """
    try:
        temp_folder = tempfile.mkdtemp(prefix="rezpy-")
        nuget_path = os.path.join(temp_folder, "nuget.exe")
        log.info("Downloading nuget to temporary path")
        urllib.request.urlretrieve(
            "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe", nuget_path
        )
        try:
            log.info("Installing python into temporary path")
            cmd = [
                nuget_path,
                "install",
                "python",
                "-OutputDirectory",
                temp_folder,
                "-Version",
                python_version,
            ]

            subprocess.run(
                cmd,
                shell=True,
                check=True,
                capture_output=True,
            )
        except Exception as e:
            raise OSError("Installation failed: " + str(e.stderr))

        source_path = os.path.join(temp_folder, "python." + python_version, "tools")

        def make_root(variant, path):
            distutils.dir_util.copy_tree(source_path, path)

        with make_package("python", packages_path, make_root=make_root) as pkg:
            pkg.version = python_version
            pkg.description = "Python programming language"
            pkg.authors = ["Python Software Foundation"]
            pkg.uuid = "8c94dcaa-404f-44c7-9ede-25fbb932b98d"
            pkg.homepage = "http://www.python.org"
            pkg.variants = [["platform-windows", "arch-AMD64"]]
            pkg.commands = """import os
env.PATH.append(this.root)
env.PATH.append(os.path.join(this.root, "DLLs"))
"""
    except Exception as e:
        log.error(e)

    finally:
        log.info("Remove temporary folder -> " + temp_folder)
        shutil.rmtree(temp_folder)
