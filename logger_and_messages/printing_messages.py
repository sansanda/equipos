from termcolor import colored

def printMessage(message, headerStr, footerStr):
    print("\n")
    print(colored(len(message) * headerStr, "magenta"))
    print(colored(message, "magenta"))
    print(colored(len(message) * footerStr, "magenta"))
    print("\n")