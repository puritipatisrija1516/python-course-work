import os
import re

# Folder for complaints
COMPLAINTS_DIR = "complaints"
if not os.path.exists(COMPLAINTS_DIR):
    os.makedirs(COMPLAINTS_DIR)

# Sentiment word lists
positive_words = ["good", "resolved", "satisfied", "happy"]
negative_words = ["bad", "poor", "unhappy", "angry", "issue"]

# Categories by keywords
categories = {
    "Billing": ["bill", "charge", "payment"],
    "Service": ["service", "support", "staff"],
    "Technical": ["network", "internet", "technical", "system"]
}

def analyze_sentiment(text):
    if any(word in text.lower() for word in negative_words):
        return "Negative"
    elif any(word in text.lower() for word in positive_words):
        return "Positive"
    else:
        return "Neutral"

def detect_category(text):
    for cat, keywords in categories.items():
        if any(re.search(rf"\b{kw}\b", text.lower()) for kw in keywords):
            return cat
    return "Other"

def create_complaint():
    name = input("Enter customer name: ")
    complaint = input("Enter complaint details: ")
    filename = f"{name.replace(' ', '_')}.txt"
    filepath = os.path.join(COMPLAINTS_DIR, filename)

    with open(filepath, "w") as f:
        f.write(f"Name: {name}\nComplaint: {complaint}\nStatus: Pending")

    print(f"Complaint saved as {filename}")

def list_complaints():
    files = os.listdir(COMPLAINTS_DIR)
    return files if files else []

def analyze_complaints():
    files = list_complaints()
    if not files:
        print("No complaints available.")
        return

    for file in files:
        with open(os.path.join(COMPLAINTS_DIR, file), "r") as f:
            text = f.read()
            sentiment = analyze_sentiment(text)
            category = detect_category(text)
            print(f"\nFile: {file}")
            print(f"Category: {category}")
            print(f"Sentiment: {sentiment}")
            print(text)

def modify_complaint():
    files = list_complaints()
    if not files:
        print("No complaints available.")
        return
    
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    
    choice = int(input("Choose a complaint to modify: ")) - 1
    filepath = os.path.join(COMPLAINTS_DIR, files[choice])

    with open(filepath, "r") as f:
        content = f.read()

    print("\nCurrent Complaint:\n", content)
    new_status = input("Enter new status (Pending/Resolved): ")

    content = re.sub(r"Status: .*", f"Status: {new_status}", content)

    with open(filepath, "w") as f:
        f.write(content)

    print("Complaint updated successfully.")

def search_complaint():
    keyword = input("Enter keyword to search: ").lower()
    files = list_complaints()
    found = False

    for file in files:
        with open(os.path.join(COMPLAINTS_DIR, file), "r") as f:
            text = f.read().lower()
            if keyword in text:
                print(f"\nFound in {file}:")
                print(text)
                found = True

    if not found:
        print("No complaints found with that keyword.")

def main():
    while True:
        print("\n📌 Complaint Management System")
        print("1. Create New Complaint")
        print("2. Analyze Complaints")
        print("3. Modify Complaint")
        print("4. Search Complaints")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_complaint()
        elif choice == "2":
            analyze_complaints()
        elif choice == "3":
            modify_complaint()
        elif choice == "4":
            search_complaint()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    create_complaint()