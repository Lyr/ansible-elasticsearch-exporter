Ansible Elasticsearch Exporter Role
============

[![Build Status](https://travis-ci.org/Lyr/ansible-elasticsearch-exporter.svg?branch=master)](https://travis-ci.org/Lyr/ansible-elasticsearch-exporter)

An Ansible Role that installs [Prometheus Elasticsearch Exporter](https://github.com/justwatchcom/elasticsearch_exporter) on Linux (default versions 1.1.0).

## Role Variables

Available variables with their default values are defined in [defaults/main.yml](defaults/main.yml).

## Supported Platform

Checkout [Test TravisCI Molecule configuration](/.travis.yml) to see what platforms are supported and tested.

## Test

Install required dependencies:

	pip install  install ansible molecule==3.0.6 yamllint ansible-lint==4.2.0 docker==4.2.2 testinfra==5.2.2

Run tests:

	molecule test -s default


## License

Author: Lyr

Licensed under the Apache License V2.0. See the [LICENSE file](LICENSE) for details.
