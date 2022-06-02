## Introduction

rezify_python is a command line utility to release python versions as rez
package.

### Usage

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