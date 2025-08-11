def get_messages():
    messages = []
    num = int(input("Enter the number of messages: "))
    for _ in range(num):
        msg = input()
        if ": " in msg:
            messages.append(msg)
        else:
            print("Invalid format. Use 'Name: message'")
    return messages

def extract_user_and_text(messages):
    data = []
    for msg in messages:
        if ": " in msg:
            name, text = msg.split(": ", 1)
            data.append((name.strip(), text.strip()))
    return data

def count_total_messages(messages):
    print("Total messages:", len(messages))

def identify_unique_users(data):
    users = {name for name, _ in data}
    print("Unique users in the chat:", users)

def count_total_words(data):
    total_words = sum(len(text.split()) for _, text in data)
    print("Total words in the chat:", total_words)

def average_words_per_message(data):
    avg = sum(len(text.split()) for _, text in data) / len(data)
    print(f"Average words per message: {avg:.2f}")

def find_longest_message(messages):
    longest = max(messages, key=lambda msg: len(msg))
    print("Longest message:", longest)

def most_active_user(data):
    from collections import Counter
    counter = Counter(name for name, _ in data)
    user, count = counter.most_common(1)[0]
    print(f"Most active user: {user} ({count} messages)")

def message_count_for_user(data):
    user = input("Input: ").strip()
    count = sum(1 for name, _ in data if name == user)
    print(f"Messages sent by {user}: {count}")

def most_frequent_word_by_user(data):
    from collections import Counter
    user = input("Input: ").strip()
    words = []
    for name, text in data:
        if name == user:
            words.extend(text.lower().split())
    if words:
        word, _ = Counter(words).most_common(1)[0]
        print(f'Most frequent word used by {user}: "{word}"')
    else:
        print(f"No messages from {user}")

def first_and_last_message(data):
    user = input("Input: ").strip()
    user_msgs = [f"{name}: {text}" for name, text in data if name == user]
    if user_msgs:
        print("First message by", user + ":", user_msgs[0])
        print("Last message by", user + ":", user_msgs[-1])
    else:
        print(f"No messages from {user}")

def check_user_presence(data):
    user = input("Input: ").strip()
    if any(name == user for name, _ in data):
        print(f"User '{user}' is present in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def commonly_repeated_words(data):
    from collections import Counter
    all_words = [word.lower() for _, text in data for word in text.split()]
    word_counts = Counter(all_words)
    common = {word for word, count in word_counts.items() if count > 1}
    print("Common repeated words:", common)

def user_with_longest_avg_msg(data):
    from collections import defaultdict
    user_words = defaultdict(list)
    for name, text in data:
        user_words[name].append(len(text.split()))
    avg_lengths = {user: sum(lengths) / len(lengths) for user, lengths in user_words.items()}
    user = max(avg_lengths, key=avg_lengths.get)
    print(f"User with longest average message: {user} (avg {avg_lengths[user]:.1f} words)")

def messages_mentioning_user(data):
    mention = input("Input: ").strip().lower()
    count = sum(1 for _, text in data if mention in text.lower())
    print(f"Messages mentioning '{mention}': {count}")

def remove_duplicate_messages(messages):
    unique_msgs = list(dict.fromkeys(messages))
    print("Unique messages count:", len(unique_msgs))
    for msg in unique_msgs:
        print(msg)

def sort_messages(messages):
    for msg in sorted(messages):
        print(msg)

def extract_questions(data):
    questions = [f"{name}: {text}" for name, text in data if "?" in text]
    for q in questions:
        print(q)

def reply_ratio(data):
    user1 = input("Input user 1: ").strip()
    user2 = input("Input user 2: ").strip()
    ratio = 0
    for i in range(1, len(data)):
        if data[i-1][0] == user1 and data[i][0] == user2:
            ratio += 1
    print(f"Reply ratio from {user2} to {user1}: {ratio} replies")

def check_deleted_messages(data):
    count = sum(1 for _, text in data if text.lower() == "this message was deleted")
    print(f"Deleted messages found: {count}")

def main():
    messages = get_messages()
    data = extract_user_and_text(messages)

    options = {
        1: lambda: count_total_messages(messages),
        2: lambda: identify_unique_users(data),
        3: lambda: count_total_words(data),
        4: lambda: average_words_per_message(data),
        5: lambda: find_longest_message(messages),
        6: lambda: most_active_user(data),
        7: lambda: message_count_for_user(data),
        8: lambda: most_frequent_word_by_user(data),
        9: lambda: first_and_last_message(data),
        10: lambda: check_user_presence(data),
        11: lambda: commonly_repeated_words(data),
        13: lambda: user_with_longest_avg_msg(data),
        14: lambda: messages_mentioning_user(data),
        15: lambda: remove_duplicate_messages(messages),
        16: lambda: sort_messages(messages),
        17: lambda: extract_questions(data),
        18: lambda: reply_ratio(data),
        19: lambda: check_deleted_messages(data)
    }

    while True:
        print("\nChoose an option (1-19) or 0 to exit:")
        choice = int(input())
        if choice == 0:
            break
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
