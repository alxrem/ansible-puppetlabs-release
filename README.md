[![Build Status](https://travis-ci.org/alxrem/ansible-puppetlabs-release.svg?branch=master)](https://travis-ci.org/alxrem/ansible-puppetlabs-release)

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
