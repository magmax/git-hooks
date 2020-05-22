#!/usr/bin/env python

import re
import subprocess
import sys



def get_last_commit_message():
    return subprocess.check_output(["git", "log", "-1", "--pretty=%B"])


def valid_commit_message(project_key, message):
    project_key_regex = "^%s-[0-9]+(.*)$" % project_key
    merge_regex = "^Merge (.*)$"
    revert_regex = "^Revert (.*)$"
    if re.match(project_key_regex, message) or re.match(merge_regex, message) or re.match(revert_regex, message):
        return True

    print("\033[1;31;40mERROR:\033[0m Missing Jira issue number in commmit message. And not merge or revert automatic message.")
    print("\033[1;32;40mLast valid commit message:\033[0m %s" % get_last_commit_message().rstrip().decode())
    print("Example: \"%s-3323: some text\"" % project_key)

    return False

def main():
    message_file = sys.argv[1]
    project_key = sys.argv[2]

    with open(message_file) as fd:
        commit_message = fd.read()

    if not valid_commit_message(project_key, commit_message):
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
