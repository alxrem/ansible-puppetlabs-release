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
