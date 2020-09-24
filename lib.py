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

if __name__ == "__main__":
    pass
