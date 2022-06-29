## Introduction

rezify_python is a command line utility to release python versions as rez
package.

### Installation

Clone the repository and install using pip:
```
pip install .
```

### Usage

Note: the version needs to be given as exact version e.g. 3.8.9, partial versions like 3.7 will not work (due to the way nuget handles these requests). You can find a full list of supported releases here: https://www.nuget.org/packages/python/

Support for releasing python-2.x releases will be added soon.

```
Usage: rezpy [OPTIONS]

Options:
  -r, --release              Release to release path instead of local path
  -p, --packages_path TEXT   Release to custom path, overrides --release
  -v, --python_version TEXT  Release specific version (latest if not set)
                             [required]
  --help                     Show this message and exit.
```

If no custom path is given the cli uses the rez configured local or release
packages path.
