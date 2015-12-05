#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 et

import unittest
from subprocess import check_output
import re


class AnsibleTestCase(unittest.TestCase):
    RESULT_RE = re.compile(
        r'(\w+)\s*:\s*'
        r'ok=(\d+)\s+changed=(\d+)\s+unreachable=(\d+)\s+failed=(\d+)',
        )

    def setUp(self):
        check_output('vagrant up'.split())
        self.ansible_playbook('test.yml')

    def tearDown(self):
        check_output('vagrant destroy -f'.split())

    def ansible_playbook(self, playbook):
        self._ansible_results = dict()
        stdout = check_output(['ansible-playbook', playbook])
        for results in AnsibleTestCase.RESULT_RE.findall(stdout):
            self._ansible_results[results[0]] = dict(zip(
                'ok changed unreachable failed'.split(),
                [int(counter) for counter in results[1:]]))

    def assertAnsibleResults(self, **kwargs):
        for host, results in self._ansible_results.items():
            for status, counter in results.items():
                if status not in kwargs:
                    continue
                expected = kwargs[status]
                self.assertEqual(
                    counter, expected,
                    'Expected {0} tasks were {1} on host {2}, '
                    'got {3}'.format(expected, status, host, counter))


class TestRole(AnsibleTestCase):
    def test_install_package_on_clean_system(self):
        self.assertAnsibleResults(ok=2, changed=2)

    def test_idempotency(self):
        self.ansible_playbook('test.yml')
        self.assertAnsibleResults(ok=1, changed=0)

    def test_reinstall_package(self):
        self.ansible_playbook('remove_package.yml')
        self.ansible_playbook('test.yml')
        self.assertAnsibleResults(ok=2, changed=2)


if __name__ == '__main__':
    unittest.main()
