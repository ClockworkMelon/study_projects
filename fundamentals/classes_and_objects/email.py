class Email:
    def __init__(self, sender, received, content):
        self.sender = sender
        self.received = received
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.received}: {self.content}. Sent: {self.is_sent}'

emails = []

while True:
    line = input().split()

    if line[0] == "Stop":
        break

    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(", ")))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())