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

temp_folder = tempfile.mkdtemp(prefix="rezpy-")
nuget_path = os.path.join(temp_folder, "nuget.exe")
python_version = "3.8.0"
install_path = r"C:\Users\insti\packages"

try:
    log.info("Downloading nuget to temporary path")
    urllib.request.urlretrieve(
        "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe", nuget_path
    )
    log.info("Installing python into temporary path")
    output = subprocess.run(
        [
            nuget_path,
            "install",
            "python",
            "-Version",
            python_version,
            "-OutputDirectory",
            temp_folder,
        ],
        shell=True,
        check=True,
        capture_output=True,
    )
    source_path = os.path.join(temp_folder, "python." + python_version, "tools")

    def make_root(variant, path):
        distutils.dir_util.copy_tree(source_path, path)

    with make_package("python", install_path, make_root=make_root) as pkg:
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
    print(e)

finally:
    log.info("Remove temporary folder")
    log.info(temp_folder)
    #shutil.rmtree(temp_folder)
