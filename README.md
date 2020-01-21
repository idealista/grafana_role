![Logo](https://raw.githubusercontent.com/idealista/grafana_role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/grafana_role.png)](https://travis-ci.org/idealista/grafana_role)

# Prometheus Grafana Ansible role

This ansible role installs an Grafana server in a debian environment.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an [Grafana](https://grafana.net/) server in a Debian system.

### Prerequisities

Ansible 2.8.x.x version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver. Pipenv 2018.11.26 and Python 3 recommended.

### Installing

Create or add to your roles dependency file (e.g requirements.yml) from GitHub:

```
- src: http://github.com/idealista/grafana_role.git
  scm: git
  version: 1.3.0
  name: grafana
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/grafana_role/) as origin if you prefer:

```
- src: idealista.grafana_role
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - grafana
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

You can edit grafana config and dashboards via template or webui.

## Testing

```
pipenv shell
pipenv sync
molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/grafana_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista-tech/grafana/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
