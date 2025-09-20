from data import Voter, Candidate, VotingSystem

def main():
    system = VotingSystem()
    print(VotingSystem.system_info())

    # ---- Sample Data ----
    system.register_voter(Voter("Ravi", "9876543210", "V001"))
    system.register_voter(Voter("Sita", "9876500000", "V002"))

    system.register_candidate(Candidate("Arjun", "9998887777", "Party A"))
    system.register_candidate(Candidate("Meera", "8887776666", "Party B"))

    while True:
        print("\n--- MENU ---")
        print("1. Show Voters")
        print("2. Show Candidates")
        print("3. Cast Vote")
        print("4. Show Results")
        print("5. Show Total Votes")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            for v in system.voters:
                print(v.display_info())
        elif choice == "2":
            for c in system.candidates:
                print(c.display_info())
        elif choice == "3":
            voter_id = input("Enter Voter ID: ")
            candidate_name = input("Enter Candidate Name: ")
            system.cast_vote(voter_id, candidate_name)
        elif choice == "4":
            system.show_results()
        elif choice == "5":
            print(VotingSystem.show_total_votes())
        elif choice == "6":
            print("Exiting... Thank you for voting!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "_main_":
    main()