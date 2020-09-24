#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete
import subprocess


def get_contact_list():
    contacts = subprocess.check_output("termux-contact-list", shell=True)
    contacts = eval(contacts)
    contacts = {contact["name"]: contact["number"].replace(" ", "") for contact in contacts}
    return contacts

def make_call(contact_name):
    contacts = get_contact_list()
    try:
        phone_number = contacts[contact_name]
    except KeyError:
        raise RuntimeError("Contact {} was not found".format(contact_name))
    subprocess.call("termux-telephony-call {}".format(phone_number), shell=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--contact_name", choices=get_contact_list().keys())
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    make_call(args.contact_name)


if __name__ == "__main__":
    main()
