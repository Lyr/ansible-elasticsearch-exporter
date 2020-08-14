"""Role testing files using testinfra."""

def test_exporter_running_and_enabled(host):
    exporter = host.service('elasticsearch-exporter')
    assert exporter.is_running
    assert exporter.is_enabled


def test_exporter_http(host):
    assert host.socket("tcp://0.0.0.0:9108").is_listening
    command = """curl -v http://localhost:9108/metrics"""
    cmd = host.run(command)
    assert '# HELP elasticsearch_cluster' in cmd.stdout