# Grafana Role

This role installs grafana with MySQL as backend using http://git/projects/AS/repos/mysql-role

To test it

```bash
cd tests
vagrant up
```

To check the installation grafana is running on 10.0.0.2:8080, log with your ldap credentials or grafana admin user.

You can edit grafana config and dashboards via template or webui.
