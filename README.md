[![Ansible Galaxy](https://img.shields.io/ansible/role/6371.svg)](https://galaxy.ansible.com/detail#/role/6371)

puppetlabs-release
==================

Role installs release package from Puppetlabs repository.

No parameters, no dependencies.

Intended to use as dependency of other roles related to puppet.

Supported platforms are

- Debian wheezy
- Debian jessie
- Ubuntu precise (12.04 LTS)
- Ubuntu trusty (14.04 LTS)

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
