import os
import pickle

if not os.path.isfile("email.dat"):
    google_email = input("Enter email: ")
    pickle.dump(google_email, open("email.dat", "wb"))

if not os.path.isfile("mail_password.dat"):
    mail_password = input("Email's generated app password: ")
    pickle.dump(mail_password, open("mail_password.dat", "wb"))
