#Here in this code we are gonna slice an email address into user,domain and extention.
def email_slicer():
    print("Here we are gonna slice the email address into three components")
    email = input("Email address: ")
    user,domain = email.split("@")
    domain,extention = domain.split(".")

    print(
        f"User: {user}\nDomain: {domain}\nExtention: {extention}"
    )

email_slicer()