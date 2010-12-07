#!/usr/bin/env python

""" Absolum:Email

Send emails based on example from the website:
ginstrom.com/scribbles/2009/03/15/a-module-to-send-email-simply-in-python

"""
import mailer

class Sender(object):

    def __init__(self):
        pass
    
    def test(self):
        message = mailer.Message()
        message.From = "Jose.Torres@8bc.org"
        message.To = "Jose.Torres@8bc.org"
        message.Subject = "My Test Python Email"    
        message.Body = "Hello Jose" # open("letter.txt", "rb").read()

        my_mailer = mailer.Mailer("outgoing.verizon.net")
        my_mailer.send(message)
        
        
if __name__ == "__main__":
    send = Sender()
    send.test()
        

