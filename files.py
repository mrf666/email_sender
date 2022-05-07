def get_emails():
   with open('emails.txt', 'r') as f:
      emails = f.read().split("\n")
      return emails


