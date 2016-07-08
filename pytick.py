#!/usr/bin/env python3

import subprocess
import getpass
import os
import datetime
import sys

__author__ = "Vimal A.R"
__email__ = "arvimal@yahoo.in"
__version__ = "0.1"

EDITOR = "/usr/bin/gedit"


class pytick(object):

    def __init__(self):
        pass

    def spacer(self, num):
        """
        Takes an integer and prints a spacer for that count

        :param num: integer
        :return: string
        """
        print(" ")
        print("-" * int(num))
        print(" ")

    def setup(self):
        """
        Setting up basic configurations here.
        Calls the pytick loop.

        :return: None
        """
        data_dir = "/home/" + getpass.getuser() + "/pytick/tickets/"
        if not os.path.exists(data_dir):
            print "\nInitial configuration\n"
            os.makedirs(data_dir)
            print "Cases will be stored in :", data_dir
            self.spacer(20)
            self.pytick_loop()
        else:
            self.pytick_loop()

    def pytick_loop(self):
        """
        The heart of `pytick`
        This is where we branch out depending on the inputs

        :return: None
        """
        while True:
            print ""
            value = raw_input("pytick >>> ")
            # How can we get tab-completion in here?
            value = value.split(" ")
            if len(value) == 1 and value[0] == "open":
                print "\n'open' needs a ticket number !!"
                self.pytick_loop()
            elif len(value) == 2 and value[0] == "open":
                self.open(value[1])
            elif value[0] == "search":
                # We call the __doc__ magic method till it's implemented.
                print(self.search.__doc__)
            elif value[0] == 'list':
                # We call the __doc__ magic method till it's implemented.
                print(self.list.__doc__)
            elif value[0] == "quit":
                sys.exit("\nExisting pytick!\n")
            else:
                self.help()

    def open(self, casenumber):
        """
        This function takes an integer as argument.
        This integer is expected to be a case/ticket number.

        :param casenumber: integer
        :return: None
        """

        try:
            value = int(casenumber)
            case = str(value)
            now = datetime.datetime.now()
            datedir = str(now.year) + "/" + str(now.month) + \
                "/" + str(now.day) + "/"
            path = "/home/" + \
                getpass.getuser() + "/pytick/tickets/" + datedir + "/"
            actualcase = path + case

            if os.path.exists(actualcase):
                subprocess.Popen((EDITOR, actualcase))
            else:
                if not os.path.exists(path):
                    os.makedirs(path)
                    with open(actualcase, 'a') as fd:
                        fd.write("Case number : \n")
                        fd.write("Subject     : \n\n")
                        fd.write("KCS         : \n\n")
                    subprocess.Popen((EDITOR, actualcase))
        except ValueError:
            print "\n'open' takes an integer value for ticket number !!"
            self.pytick_loop()

    def search(self, *args):
        """
        This helps to search for keywords in your cases.

        It will print the case number and subject line of cases with
        the searched keywords.

        Work in progress.

        :param args: search keywords
        :return: string
        """
        pass

    def list(self, *args):
        """
        This feature lists the cases, and takes in various search criteria.

        Yet to be implemented, come back in a few days.

        """
        pass

    def help(self):
        """
        Usage info
        :return: None
        """
        print ""
        print "Usage : "
        print " 1) open   <case-number> - To open a new or existing case."
        print " 2) search <key-word>    - To search an already existing case. "
        print " 3) list   <case-number> - To list cases according to dates. "
        print " 4) help                 - Prints this help message. "
        print " 5) quit                 - Quits pytick. "

if __name__ == "__main__":
    pytick_object = pytick()
    pytick_object.setup()