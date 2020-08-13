"""Role testing files using testinfra."""

def test_exporter_running_and_enabled(host):
    exporter = host.service('elasticsearch-exporter')
    assert exporter.is_running
    assert exporter.is_enabled


def test_mgmt_user_authentication(host):
    command = """curl http://localhost:9108/ """
    cmd = host.run(command)
    assert 'HTTP/1.1 200 OK' in cmd.stdout