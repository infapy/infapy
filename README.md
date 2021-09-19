# infapy

infapy is a Python library for automating with informatica cloud.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install infapy
```

## Usage

```python
import infapy

# returns 'words'
# below command to use the default profile
infaHandler=infapy.connect()

# Example to use the v2 API:
v2=infaHandler.v2()
v2.getAllActivityLog()

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache Software License](https://www.apache.org/licenses/LICENSE-2.0)