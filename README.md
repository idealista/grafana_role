![Logo](logo.gif)

# Prometheus Alert Manager Ansible role

This ansible role installs an Alert Manager server in a debian environment. The server is installed using the sources.

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

Ansible 2.2.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista-tech/grafana-role.git
  scm: git
  version: 1.0.0
  name: grafana
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
    - role: grafana
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

You can edit grafana config and dashboards via template or webui.

This role is separated in two phases.
The install cycle prepare and set up a grafana server.
The dashboards cycle imports dashboards into the server. Two kind of dashboards can be imported:
  - machine:

    This dashboard is default and you only have to set a variable to use it. An usage example can be found [here](test/group_vars/group01.yml).
  - custom:

    You can upload a custom dashboard. Just store the template int the defined `grafana_dashboard_templates_path`
    and include the variables under the `grafana_dashboards` variable like test.json.js in the [example](test/group_vars/group01.yml).

You can use only this phase by setting the tag `dashboards` in the role.
Notice that you must set the `grafana_host` and `grafana_port` vars.

```
---
- hosts: someserver
  roles:
    - role: grafana
      tags:
        - dashboard
```

## Testing

```
molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista-tech/grafana-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista-tech](https://github.com/idealista-tech)

See also the list of [contributors](https://github.com/idealista-tech/grafana-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
