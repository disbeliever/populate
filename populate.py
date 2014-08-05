#!/usr/bin/python2
#-*- coding: utf-8 -*-

import sys
import getopt


def action_fill(template):
    pass


def parse_args():
    try:
        (opts, args) = getopt.getopt(sys.argv[1:], 'h')
    except getopt.GetoptError as e:
        print "error:", e
        return

    args = args[1:]
    action = args[0]
    if (action == "fill"):
        pass
    if (len(args) > 1):
        print "warning: too many args for this action. Using only '{0}'".format(args[0])


def main():
    parse_args()
    return 0

if __name__ == "__main__":
    sys.exit(main())
