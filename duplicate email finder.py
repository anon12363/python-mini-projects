print("=== Duplicate Email Finder ===\n")
print("Paste as many emails as you want (one per line)")
print("When finished just press Enter twice\n")

emails = []
print("Start typing emails (empty line = finish):\n")

while True:
    line = input()
    if line.strip() == "":
        if emails:  # at least something was entered
            break
        else:
            print("Nothing yet... keep going or press Enter twice to quit.")
            continue
    emails.append(line.strip())

if not emails:
    print("No emails were entered. Bye! 👀")
else:
    print(f"\nYou entered {len(emails)} email addresses.\n")
    
    # ─── The magic part with sets ───
    seen = set()
    duplicates = set()
    
    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)
    
    if duplicates:
        print("🚨 Found duplicate emails:\n")
        for dup in sorted(duplicates):
            print("   •", dup)
        print()
        print(f"→ {len(duplicates)} different email(s) appear more than once")
    else:
        print("Nice! No duplicates found 🎉")
    
    print(f"→ Unique emails: {len(seen)}")
