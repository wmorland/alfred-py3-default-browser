# Py3 Default Browser

This [Alfred](https://www.alfredapp.com) workflow makes it simple to change your default
browser on macOS.

[![Download latest version](https://img.shields.io/github/v/release/wmorland/alfred-py3-default-browser?label=Download&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNy40NyAxMC43OGEuNzUuNzUgMCAwMDEuMDYgMGwzLjc1LTMuNzVhLjc1Ljc1IDAgMDAtMS4wNi0xLjA2TDguNzUgOC40NFYxLjc1YS43NS43NSAwIDAwLTEuNSAwdjYuNjlMNC43OCA1Ljk3YS43NS43NSAwIDAwLTEuMDYgMS4wNmwzLjc1IDMuNzV6TTMuNzUgMTNhLjc1Ljc1IDAgMDAwIDEuNWg4LjVhLjc1Ljc1IDAgMDAwLTEuNWgtOC41eiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D&sort=semver&style=for-the-badge&color=blue)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)

<img src=".images/Example.png" alt="Screenshot of Alfred Workflow in action" width="623" height="305"/>

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/wmorland/alfred-py3-default-browser/CodeQL?label=CodeQL&logo=github)](https://github.com/wmorland/alfred-py3-default-browser/actions/workflows/codeql-analysis.yml)
[![Dependabot](.images/badges/Dependabot%20enabled.svg)](https://github.com/wmorland/alfred-py3-default-browser/security/dependabot)
[![Alfred Workflow](.images/badges/Alfred%20Workflow.svg)](https://www.alfredapp.com/workflows/)
[![Python 3](.images/badges/Python%203.svg)](https://www.python.org)
[![Built using PyCharm](.images/badges/Built%20using%20PyCharm.svg)](https://www.jetbrains.com/pycharm/)
[![code style black](.images/badges/code%20style%20black.svg)](https://github.com/psf/black)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/wmorland/alfred-py3-default-browser?sort=semver&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDcuNzc1VjIuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDUuMDI1YS4yNS4yNSAwIDAxLjE3Ny4wNzNsNi4yNSA2LjI1YS4yNS4yNSAwIDAxMCAuMzU0bC01LjAyNSA1LjAyNWEuMjUuMjUgMCAwMS0uMzU0IDBsLTYuMjUtNi4yNWEuMjUuMjUgMCAwMS0uMDczLS4xNzd6bS0xLjUgMFYyLjc1QzEgMS43ODQgMS43ODQgMSAyLjc1IDFoNS4wMjVjLjQ2NCAwIC45MS4xODQgMS4yMzguNTEzbDYuMjUgNi4yNWExLjc1IDEuNzUgMCAwMTAgMi40NzRsLTUuMDI2IDUuMDI2YTEuNzUgMS43NSAwIDAxLTIuNDc0IDBsLTYuMjUtNi4yNUExLjc1IDEuNzUgMCAwMTEgNy43NzV6TTYgNWExIDEgMCAxMDAgMiAxIDEgMCAwMDAtMnoiPjwvcGF0aD48L3N2Zz4%3D&color=blue)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)
[![GitHub downloads all releases](https://img.shields.io/github/downloads/wmorland/alfred-py3-default-browser/total?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNy40NyAxMC43OGEuNzUuNzUgMCAwMDEuMDYgMGwzLjc1LTMuNzVhLjc1Ljc1IDAgMDAtMS4wNi0xLjA2TDguNzUgOC40NFYxLjc1YS43NS43NSAwIDAwLTEuNSAwdjYuNjlMNC43OCA1Ljk3YS43NS43NSAwIDAwLTEuMDYgMS4wNmwzLjc1IDMuNzV6TTMuNzUgMTNhLjc1Ljc1IDAgMDAwIDEuNWg4LjVhLjc1Ljc1IDAgMDAwLTEuNWgtOC41eiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D&color=blue)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)
[![GitHub stars](https://img.shields.io/github/stars/wmorland/alfred-py3-default-browser?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNOCAuMjVhLjc1Ljc1IDAgMDEuNjczLjQxOGwxLjg4MiAzLjgxNSA0LjIxLjYxMmEuNzUuNzUgMCAwMS40MTYgMS4yNzlsLTMuMDQ2IDIuOTcuNzE5IDQuMTkyYS43NS43NSAwIDAxLTEuMDg4Ljc5MUw4IDEyLjM0N2wtMy43NjYgMS45OGEuNzUuNzUgMCAwMS0xLjA4OC0uNzlsLjcyLTQuMTk0TC44MTggNi4zNzRhLjc1Ljc1IDAgMDEuNDE2LTEuMjhsNC4yMS0uNjExTDcuMzI3LjY2OEEuNzUuNzUgMCAwMTggLjI1em0wIDIuNDQ1TDYuNjE1IDUuNWEuNzUuNzUgMCAwMS0uNTY0LjQxbC0zLjA5Ny40NSAyLjI0IDIuMTg0YS43NS43NSAwIDAxLjIxNi42NjRsLS41MjggMy4wODQgMi43NjktMS40NTZhLjc1Ljc1IDAgMDEuNjk4IDBsMi43NyAxLjQ1Ni0uNTMtMy4wODRhLjc1Ljc1IDAgMDEuMjE2LS42NjRsMi4yNC0yLjE4My0zLjA5Ni0uNDVhLjc1Ljc1IDAgMDEtLjU2NC0uNDFMOCAyLjY5NHYuMDAxeiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D)](https://github.com/wmorland/alfred-py3-default-browser/stargazers)
[![GitHub license](.images/badges/license%20MIT.svg)](https://github.com/wmorland/alfred-py3-default-browser/blob/main/LICENSE)

## Installation

To install this workflow you just have to download and open the `.alfredworkflow` file
from the latest
release [here](https://github.com/wmorland/alfred-py3-default-browser/releases/latest).
The Alfred website's Help section has more information about
Workflows [here](https://www.alfredapp.com/help/workflows/#discovering). Workflows are a
paid feature of Alfred which require
the [Alfred Powerpack](https://www.alfredapp.com/powerpack/).

## Usage

The default shortcut is `db` and you can then pick a browser from the list of available
options. macOS requires you to confirm the change in a pop up dialog. For
example:

<img src=".images/Browser Confirmation.png" alt="Screenshot of the macOS confirmation dialog" width="372" height="392"/>

### Changing the Alfred keyword

1. Open Alfred Preferences and go to 'Workflows' > 'Py3 Default Browser'.
2. Double click on the Script Filter
   component.

<img src=".images/Script Filter.png" alt="Screenshot of the Script Filter" width="149" height="212"/>

3. Change the keyword field to your new chosen keyword (you can leave all other fields
   the same) and then click 'Save'.

## Support

If you have any questions or feature requests then
please [file an Issue](https://github.com/wmorland/alfred-py3-default-browser/issues/new)
on GitHub or reach out to me on Twitter, [@w_morland](https://twitter.com/w_morland).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what
you would like to change.

## Acknowledgements

Thanks to:

- [@deanishe](https://github.com/deanishe) for
  the [alfred-workflow](https://github.com/deanishe/alfred-workflow) library.
- [@NorthIsUp](https://github.com/NorthIsUp) for updating it to Python 3
  in [alfred-workflow-py3](https://github.com/NorthIsUp/alfred-workflow-py3).
- [@kerma](https://github.com/kerma) for
  the [defaultbrowser](https://github.com/kerma/defaultbrowser) tool which was a
  valuable reference.

## Security

- [SECURITY.md](.github/SECURITY.md) (Security Policy)
- [security.txt](.wellknown/security.txt) ([@securitytxt](https://github.com/securitytxt))

## License

[MIT](LICENSE)
