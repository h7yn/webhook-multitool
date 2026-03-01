import requests
import os
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_banner():
    banner = r"""

██╗░░██╗███████╗██╗░░░██╗███╗░░██╗
██║░░██║╚════██║╚██╗░██╔╝████╗░██║
███████║░░░░██╔╝░╚████╔╝░██╔██╗██║
██╔══██║░░░██╔╝░░░╚██╔╝░░██║╚████║
██║░░██║░░██╔╝░░░░░██║░░░██║░╚███║
╚═╝░░╚═╝░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══╝         

ｗｅｂｈｏｏｋ ｍｕｌｔｉｔｏｏｌ


    """
    print(Fore.BLUE + banner)

def get_webhook_info():
    """Prompts the user to enter webhook URL and returns it."""
    webhook_url = input("Enter the Discord webhook URL: ")
    return webhook_url

def send_spam_message(webhook_url):
    """Sends a specified number of messages to the webhook."""
    num_messages = int(input("How many messages do you want to send? "))
    message_content = input("Enter the message content: ")

    for _ in range(num_messages):
        payload = {'content': message_content}
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            print(Fore.RED + f"Failed to send message: {response.text}")

def rename_webhook(webhook_url):
    """Renames the webhook."""
    new_name = input("Enter the new name for the webhook: ")
    payload = {'name': new_name}
    response = requests.patch(webhook_url, json=payload)
    if response.status_code != 200:
        print(Fore.RED + f"Failed to rename webhook: {response.text}")
    else:
        print(Fore.GREEN + "Webhook renamed successfully.")

def delete_webhook(webhook_url):
    """Deletes the webhook."""
    response = requests.delete(webhook_url)
    if response.status_code == 404:
        print(Fore.RED + "Webhook not found.")
    elif response.status_code != 204:
        print(Fore.RED + f"Failed to delete webhook: {response.text}")
    else:
        print(Fore.GREEN + "Webhook deleted successfully.")

def change_webhook_pfp(webhook_url):
    """Changes the webhook profile picture."""
    image_url = input("Enter the image URL for the new avatar: ")
    payload = {'avatar': image_url}
    response = requests.patch(webhook_url, json=payload)
    if response.status_code != 200:
        print(Fore.RED + f"Failed to change webhook avatar: {response.text}")
    else:
        print(Fore.GREEN + "Webhook avatar changed successfully.")

def main():
    while True:
        clear_screen()
        ascii_banner()

        print(Fore.MAGENTA + "1. Spam message")
        print(Fore.MAGENTA + "2. Rename webhook")
        print(Fore.MAGENTA + "3. Delete webhook")
        print(Fore.MAGENTA + "4. Change webhook pfp")
        print(Fore.MAGENTA + "5. Exit program")

        choice = input("\nChoose an option: ")

        if choice == '1':
            webhook_url = get_webhook_info()
            send_spam_message(webhook_url)
        elif choice == '2':
            webhook_url = get_webhook_info()
            rename_webhook(webhook_url)
        elif choice == '3':
            webhook_url = get_webhook_info()
            delete_webhook(webhook_url)
        elif choice == '4':
            webhook_url = get_webhook_info()
            change_webhook_pfp(webhook_url)
        elif choice == '5':
            print(Fore.GREEN + "Exiting program...")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
