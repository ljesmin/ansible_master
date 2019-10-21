#!/usr/bin/python

import re
class FilterModule(object):
    def filters(self):
        return {
            'clean_ansible': self.clean_ansible,
        }

    def clean_ansible(self, cleanable ):
        cleaned = {}
        for i in cleanable:
            if i in ['omit','playbook_dir','group_names','groups','discovered_interpreter_python']:
                continue
            if re.match(r"^ansible_.*",i) is not None:
                continue
            if re.match(r"^inventory_.*",i) is not None:
                continue
            cleaned[i] = cleanable[i]
        return cleaned
