def get_welcome_message(Eric):
    return f"Welcome, {name}! We're excited to have you here! 🎉"

def main():
    print("Please enter your name:")
    name = input().strip()
    
    if name:
        message = get_welcome_message(name)
        print("\n" + message)
    else:
        print("\nWelcome, Guest! We're excited to have you here! 🎉")

if __name__ == "__main__":
    main() 
