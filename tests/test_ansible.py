import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_grafana_user(User, Group):
    assert User("grafana").exists
    assert Group("grafana").exists
    assert User("grafana").group == "grafana"


def test_grafana_conf(File, User, Group):
    conf_file = File("/etc/grafana/grafana.ini")
    assert conf_file.exists
    assert conf_file.user == "grafana"
    assert conf_file.group == "grafana"


def test_grafana_paths(File, User, Group, AnsibleDefaults):
    data_path = File(AnsibleDefaults["grafana_data_path"])
    plugins_path = File(AnsibleDefaults["grafana_plugins_path"])
    log_path = File(AnsibleDefaults["grafana_log_path"])
    assert data_path.exists
    assert data_path.is_directory
    assert data_path.user == "grafana"
    assert data_path.group == "grafana"
    assert plugins_path.exists
    assert plugins_path.is_directory
    assert plugins_path.user == "grafana"
    assert plugins_path.group == "grafana"
    assert log_path.exists
    assert log_path.is_directory
    assert log_path.user == "grafana"
    assert log_path.group == "grafana"


def test_grafana_service(File, Service, Socket, AnsibleVars):
    port = AnsibleVars["grafana_port"]
    assert Service("grafana-server").is_enabled
    assert Service("grafana-server").is_running
    assert Socket("tcp://:::" + str(port)).is_listening
