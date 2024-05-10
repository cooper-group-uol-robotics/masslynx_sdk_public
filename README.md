# Waters MassLynx SDK (version 4.7.0.0, 64 bit)
[![DOI](https://zenodo.org/badge/798701943.svg)](https://zenodo.org/doi/10.5281/zenodo.11174322)
## Obtaining code

This code is neither created nor distributed by us. I have converted it into
a Python project to make it easier to include the relevant methods in our
development code. However, the code itself cannot be re-distributed by us
and has to be obtained through the official channels:

```
https://interface.waters.com/masslynx/developers-area/sdks/
```

Note that access to the above website requires registration with Waters
and approval by Waters administrators.

## Installation and Usage

The official Waters MassLynx SDK must be unzipped and the `WatersRawSDKRedist`
folder must be placed here before running:

```
python -m pip install .
```

After installation, the SDK can simply be imported within the Python environment:

```
import masslynx
```
