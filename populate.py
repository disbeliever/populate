#!/usr/bin/python3
# -*- coding: utf-8 -*-

import getopt
import os
import shutil
import sys


def get_config_dir():
    base_dir = os.getenv('XDG_CONFIG_HOME')
    if (base_dir is None):
        base_dir = os.path.expanduser("~/.config")
    conf_dir = os.path.join(base_dir, "populate")

    return conf_dir


def action_fill(template):
    template_dir = os.path.join(get_config_dir(), template)
    if (os.path.exists(template_dir)):
        for i in os.listdir(template_dir):
            shutil.copy(os.path.join(template_dir, i), os.getcwd())
    else:
        print("error: template '{0}' doesn't exist".format(template))


def usage():
    print("Usage: " + sys.argv[0] + " action [arg]")
    print("  Where action can be:")
    print("    fill")
    print("    list")


def parse_args():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError as e:
        usage()
        sys.exit(2)

    if (len(args) == 0):
        usage()
        sys.exit(2)
    action = args[0]
    action_args = args[1:]

    if (action == "fill"):
        if (len(action_args) == 0):
            action_arg = None
            usage()
        elif (len(action_args) == 1):
            action_arg = action_args[0]
        elif (len(action_args) > 1):
            print("warning: too many args for this action. Using only '{0}'".format(args[0]))
    elif (action == "list"):
        action_arg = ''
    else:
        action_arg = None

    return action, action_arg


def main():
    (action, arg) = parse_args()
    if (action is None or arg is None):
        return

    if (action == 'fill'):
        print("Filling from template:", arg)
        action_fill(arg)
    elif (action == 'list'):
        for i in os.listdir(get_config_dir()):
            print(i)
    return 0

if __name__ == "__main__":
    sys.exit(main())
