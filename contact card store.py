print("=== My Tiny Contact Book ===\n")
print("We'll store name + phone + email as mini cards\n")

contacts = []

while True:
    print("\nWhat would you like to do?")
    print("  1 → Add new contact")
    print("  2 → Show all contacts")
    print("  3 → Quit")
    
    choice = input("→ ").strip()
    
    if choice == '3' or choice.lower().startswith('q'):
        print("\nSee you next time! 👋")
        break
        
    elif choice == '1':
        name = input("Full name: ").strip()
        phone = input("Phone number: ").strip()
        email = input("Email: ").strip()
        
        # We use tuple → (name, phone, email)
        card = (name, phone, email)
        contacts.append(card)
        print(f"\nSaved → {name}\n")
        
    elif choice == '2':
        if not contacts:
            print("Your contact book is empty right now... 🌿")
        else:
            print("\n" + "═"*50)
            print("  Your contacts")
            print("═"*50)
            
            for person in contacts:
                name, phone, email = person   # unpacking tuple
                print(f"• {name}")
                print(f"  📞 {phone}")
                print(f"  ✉️ {email}")
                print("-"*48)
                
    else:
        print("Just 1, 2 or 3 please~")
