[![Build Status](https://travis-ci.org/alxrem/ansible-puppetlabs-release.svg?branch=master)](https://travis-ci.org/alxrem/ansible-puppetlabs-release)
[![Ansible Galaxy](https://img.shields.io/ansible/role/6371.svg)](https://galaxy.ansible.com/detail#/role/6371)

puppetlabs-release
==================

Role installs release package from Puppetlabs repository.

No parameters, no dependencies.

Intended to use as dependency of other roles related to puppet.

Example playbook
----------------

```yaml
---
- hosts: puppet.example.org
  roles:
  - alxrem.puppetlabs-release
```

License
-------

GPL-3+
