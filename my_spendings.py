import tkinter as tk
import imaplib
import email
from email.header import decode_header
import webbrowser
import os

root = tk.Tk()
root.title("Get Spendings")
root.geometry("240x100")

username = tk.Entry(root, width=25, borderwidth=2)
username_label = tk.Label(root, text="Email:")

password = tk.Entry(root, show="*", width=25, borderwidth=2)
password_label = tk.Label(root, text="Password:")
#username.insert(0, "johnsmith69@gmail.com")
#password.insert(0, "")
username_label.grid(row=0, column=0)
username.grid(row=0,column=1)
password_label.grid(row=1, column=0)
password.grid(row=1,column=1)

def clean(text):
    # clean text for creating folder
    return "".join(c if c.isalnum() else "_" for c in text)


def clickButton():
    #run the function for getting email from smtp
    print("Retrieving Email..." + " Please Wait a while")
    un = username.get()
    pw = password.get()
    # create IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate with username and password
    imap.login(un,pw)
    print("Login Success!")
   #print(imap.list()) #shows a list of what imap can retrieve from
    status, count = imap.select("[Gmail]/Starred")
    # define the number of mails to retrieve under here
    N = 50
    # total number of emails
    count = int(count[0])
    
    # loop through the list of emails
    for i in range(count, count-N, -1):
        #fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse the bytes of the email into a object called msg
                msg = email.message_from_bytes(response[1])
                # find out what can be extracted
                msg.keys()
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode it to a string
                    subject = subject.decode(encoding)
                
                # decode email sender
                # From, encoding = decode_header(msg.get("From"))[0]
                # if isinstance(From, bytes):
                #     From = From.decode(encoding)
                print("Subject:", subject)
                # keyphrase to look out for, it it does not match, do not decode anything
                phrase = "Your Google Play Order"
                # only look into emails with this specific subject header
                if phrase in subject:
                    # print("From:", From)
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over the email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                # print(body)
                                if(body.find("*Order date:*") != -1): #for older google play emails
                                    print(body[body.find("*Order date:* "):body.find("SGT") + 3]) #older field of order date
                                    if(body.find("ItemPrice") == -1):
                                        print(body[body.find("Item Price"):body.find("Total:")]) #item name
                                    else:
                                        print(body[body.find("ItemPrice"):body.find("Total:")]) #item name
                                else:
                                    print(body[body.find("Order date: "):body.find("SGT") + 3]) #order date
                                    print(body[body.find("Item Price"):body.find("Total:")]) #item name
                                print(body[body.find("You've made a purchase from"):body.find("on Google Play.")]) #company name
                            # elif "attachment" in content_disposition:
                            #     # download attachment
                            #     filename = part.get_filename()
                            #     if filename:
                            #         folder_name = clean(subject)
                            #         if not os.path.isdir(folder_name):
                            #             # make a folder for this email (named after the subject)
                            #             os.mkdir(folder_name)
                            #         filepath = os.path.join(folder_name, filename)
                            #         # download attachment and save it
                            #         open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            #print(body)
                            if(body.find("*Order date:*") != -1): #for older google play emails
                                print(body[body.find("*Order date:* "):body.find("SGT") + 3]) #older field of order date
                                if(body.find("ItemPrice") == -1):
                                    print(body[body.find("Item Price"):body.find("Total:")]) #item name
                                else:
                                    print(body[body.find("ItemPrice"):body.find("Total:")]) #item name
                            else:
                                print(body[body.find("Order date: "):body.find("SGT") + 3]) #order date
                                print(body[body.find("Item Price"):body.find("Total:")]) #item name
                            print(body[body.find("You've made a purchase from"):body.find("on Google Play.")]) #company name

                    #if content_type == "text/html":
                        # if it's html, create a new html file and open it in browser
                        # print(body)
                        # return
    #print(type(body)) | determined that body is a string
    # close the connection and logout
    imap.close()
    imap.logout()





myButton = tk.Button(root, text="Confirm", command=clickButton)
myButton.grid(row=2,column=1)
root.mainloop()
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()
    
#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me faggot)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side = "top")

#         self.quit = tk.Button(self, text="Close this shit", fg="red", command = self.master.destroy)
#         self.quit.pack(side = "bottom")
    
#     def say_hi(self):
#         print("Hi nigger")
    
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()

