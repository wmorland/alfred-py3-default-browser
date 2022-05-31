# Py3 Default Browser

This [Alfred](https://www.alfredapp.com) workflow makes it simple to change your default
browser on macOS.

[![Download latest version](https://img.shields.io/github/v/release/wmorland/alfred-py3-default-browser?label=Download&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNy40NyAxMC43OGEuNzUuNzUgMCAwMDEuMDYgMGwzLjc1LTMuNzVhLjc1Ljc1IDAgMDAtMS4wNi0xLjA2TDguNzUgOC40NFYxLjc1YS43NS43NSAwIDAwLTEuNSAwdjYuNjlMNC43OCA1Ljk3YS43NS43NSAwIDAwLTEuMDYgMS4wNmwzLjc1IDMuNzV6TTMuNzUgMTNhLjc1Ljc1IDAgMDAwIDEuNWg4LjVhLjc1Ljc1IDAgMDAwLTEuNWgtOC41eiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D&sort=semver&style=for-the-badge)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)

<img src=".images/Example.png" alt="Screenshot of Alfred Workflow in action" width="623" height="305"/>

[![CodeQL](https://github.com/wmorland/alfred-py3-default-browser/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/wmorland/alfred-py3-default-browser/actions/workflows/codeql-analysis.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-success?logo=dependabot)](https://github.com/wmorland/alfred-py3-default-browser/security/dependabot)
[![Alfred Workflow](https://img.shields.io/badge/Alfred%20Workflow-5c1f87?logo=alfred&logoColor=white)](https://www.alfredapp.com/workflows/)
[![Python 3](https://img.shields.io/badge/Python%203-FFD43B?logo=python&logoColor=blue)](https://www.python.org)
[![code style black](https://img.shields.io/badge/code%20style-black-000000?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTEuMDEzIDEuNDI3YTEuNzUgMS43NSAwIDAxMi40NzQgMGwxLjA4NiAxLjA4NmExLjc1IDEuNzUgMCAwMTAgMi40NzRsLTguNjEgOC42MWMtLjIxLjIxLS40Ny4zNjQtLjc1Ni40NDVsLTMuMjUxLjkzYS43NS43NSAwIDAxLS45MjctLjkyOGwuOTI5LTMuMjVhMS43NSAxLjc1IDAgMDEuNDQ1LS43NThsOC42MS04LjYxem0xLjQxNCAxLjA2YS4yNS4yNSAwIDAwLS4zNTQgMEwxMC44MTEgMy43NWwxLjQzOSAxLjQ0IDEuMjYzLTEuMjYzYS4yNS4yNSAwIDAwMC0uMzU0bC0xLjA4Ni0xLjA4NnpNMTEuMTg5IDYuMjVMOS43NSA0LjgxbC02LjI4NiA2LjI4N2EuMjUuMjUgMCAwMC0uMDY0LjEwOGwtLjU1OCAxLjk1MyAxLjk1My0uNTU4YS4yNDkuMjQ5IDAgMDAuMTA4LS4wNjRsNi4yODYtNi4yODZ6Ij48L3BhdGg%2BPC9zdmc%2B)](https://github.com/psf/black)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/wmorland/alfred-py3-default-browser?sort=semver&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDcuNzc1VjIuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDUuMDI1YS4yNS4yNSAwIDAxLjE3Ny4wNzNsNi4yNSA2LjI1YS4yNS4yNSAwIDAxMCAuMzU0bC01LjAyNSA1LjAyNWEuMjUuMjUgMCAwMS0uMzU0IDBsLTYuMjUtNi4yNWEuMjUuMjUgMCAwMS0uMDczLS4xNzd6bS0xLjUgMFYyLjc1QzEgMS43ODQgMS43ODQgMSAyLjc1IDFoNS4wMjVjLjQ2NCAwIC45MS4xODQgMS4yMzguNTEzbDYuMjUgNi4yNWExLjc1IDEuNzUgMCAwMTAgMi40NzRsLTUuMDI2IDUuMDI2YTEuNzUgMS43NSAwIDAxLTIuNDc0IDBsLTYuMjUtNi4yNUExLjc1IDEuNzUgMCAwMTEgNy43NzV6TTYgNWExIDEgMCAxMDAgMiAxIDEgMCAwMDAtMnoiPjwvcGF0aD48L3N2Zz4%3D)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)
[![GitHub downloads all releases](https://img.shields.io/github/downloads/wmorland/alfred-py3-default-browser/total?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNy40NyAxMC43OGEuNzUuNzUgMCAwMDEuMDYgMGwzLjc1LTMuNzVhLjc1Ljc1IDAgMDAtMS4wNi0xLjA2TDguNzUgOC40NFYxLjc1YS43NS43NSAwIDAwLTEuNSAwdjYuNjlMNC43OCA1Ljk3YS43NS43NSAwIDAwLTEuMDYgMS4wNmwzLjc1IDMuNzV6TTMuNzUgMTNhLjc1Ljc1IDAgMDAwIDEuNWg4LjVhLjc1Ljc1IDAgMDAwLTEuNWgtOC41eiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D)](https://github.com/wmorland/alfred-py3-default-browser/releases/latest/download/py3-default-browser.alfredworkflow)
[![GitHub stars](https://img.shields.io/github/stars/wmorland/alfred-py3-default-browser?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNOCAuMjVhLjc1Ljc1IDAgMDEuNjczLjQxOGwxLjg4MiAzLjgxNSA0LjIxLjYxMmEuNzUuNzUgMCAwMS40MTYgMS4yNzlsLTMuMDQ2IDIuOTcuNzE5IDQuMTkyYS43NS43NSAwIDAxLTEuMDg4Ljc5MUw4IDEyLjM0N2wtMy43NjYgMS45OGEuNzUuNzUgMCAwMS0xLjA4OC0uNzlsLjcyLTQuMTk0TC44MTggNi4zNzRhLjc1Ljc1IDAgMDEuNDE2LTEuMjhsNC4yMS0uNjExTDcuMzI3LjY2OEEuNzUuNzUgMCAwMTggLjI1em0wIDIuNDQ1TDYuNjE1IDUuNWEuNzUuNzUgMCAwMS0uNTY0LjQxbC0zLjA5Ny40NSAyLjI0IDIuMTg0YS43NS43NSAwIDAxLjIxNi42NjRsLS41MjggMy4wODQgMi43NjktMS40NTZhLjc1Ljc1IDAgMDEuNjk4IDBsMi43NyAxLjQ1Ni0uNTMtMy4wODRhLjc1Ljc1IDAgMDEuMjE2LS42NjRsMi4yNC0yLjE4My0zLjA5Ni0uNDVhLjc1Ljc1IDAgMDEtLjU2NC0uNDFMOCAyLjY5NHYuMDAxeiI%2BPC9wYXRoPjwvc3ZnPg%3D%3D)](https://github.com/wmorland/alfred-py3-default-browser/stargazers)
[![GitHub license](https://img.shields.io/github/license/wmorland/alfred-py3-default-browser?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNOC43NS43NWEuNzUuNzUgMCAwMC0xLjUgMFYyaC0uOTg0Yy0uMzA1IDAtLjYwNC4wOC0uODY5LjIzbC0xLjI4OC43MzdBLjI1LjI1IDAgMDEzLjk4NCAzSDEuNzVhLjc1Ljc1IDAgMDAwIDEuNWguNDI4TC4wNjYgOS4xOTJhLjc1Ljc1IDAgMDAuMTU0LjgzOGwuNTMtLjUzLS41My41M3YuMDAxbC4wMDIuMDAyLjAwMi4wMDIuMDA2LjAwNi4wMTYuMDE1LjA0NS4wNGEzLjUxNCAzLjUxNCAwIDAwLjY4Ni40NUE0LjQ5MiA0LjQ5MiAwIDAwMyAxMWMuODggMCAxLjU1Ni0uMjIgMi4wMjMtLjQ1NGEzLjUxNSAzLjUxNSAwIDAwLjY4Ni0uNDVsLjA0NS0uMDQuMDE2LS4wMTUuMDA2LS4wMDYuMDAyLS4wMDIuMDAxLS4wMDJMNS4yNSA5LjVsLjUzLjUzYS43NS43NSAwIDAwLjE1NC0uODM4TDMuODIyIDQuNWguMTYyYy4zMDUgMCAuNjA0LS4wOC44NjktLjIzbDEuMjg5LS43MzdhLjI1LjI1IDAgMDEuMTI0LS4wMzNoLjk4NFYxM2gtMi41YS43NS43NSAwIDAwMCAxLjVoNi41YS43NS43NSAwIDAwMC0xLjVoLTIuNVYzLjVoLjk4NGEuMjUuMjUgMCAwMS4xMjQuMDMzbDEuMjkuNzM2Yy4yNjQuMTUyLjU2My4yMzEuODY4LjIzMWguMTYybC0yLjExMiA0LjY5MmEuNzUuNzUgMCAwMC4xNTQuODM4bC41My0uNTMtLjUzLjUzdi4wMDFsLjAwMi4wMDIuMDAyLjAwMi4wMDYuMDA2LjAxNi4wMTUuMDQ1LjA0YTMuNTE3IDMuNTE3IDAgMDAuNjg2LjQ1QTQuNDkyIDQuNDkyIDAgMDAxMyAxMWMuODggMCAxLjU1Ni0uMjIgMi4wMjMtLjQ1NGEzLjUxMiAzLjUxMiAwIDAwLjY4Ni0uNDVsLjA0NS0uMDQuMDEtLjAxLjAwNi0uMDA1LjAwNi0uMDA2LjAwMi0uMDAyLjAwMS0uMDAyLS41MjktLjUzMS41My41M2EuNzUuNzUgMCAwMC4xNTQtLjgzOEwxMy44MjMgNC41aC40MjdhLjc1Ljc1IDAgMDAwLTEuNWgtMi4yMzRhLjI1LjI1IDAgMDEtLjEyNC0uMDMzbC0xLjI5LS43MzZBMS43NSAxLjc1IDAgMDA5LjczNSAySDguNzVWLjc1ek0xLjY5NSA5LjIyN2MuMjg1LjEzNS43MTguMjczIDEuMzA1LjI3M3MxLjAyLS4xMzggMS4zMDUtLjI3M0wzIDYuMzI3bC0xLjMwNSAyLjl6bTEwIDBjLjI4NS4xMzUuNzE4LjI3MyAxLjMwNS4yNzNzMS4wMi0uMTM4IDEuMzA1LS4yNzNMMTMgNi4zMjdsLTEuMzA1IDIuOXoiPjwvcGF0aD48L3N2Zz4%3D)](https://github.com/wmorland/alfred-py3-default-browser/blob/main/LICENSE)

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
