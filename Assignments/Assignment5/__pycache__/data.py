from abc import ABC, abstractmethod
# ---------------- Base Class ----------------
class Person(ABC):
    def _init_(self, name, contact):
        self._name = name              # Encapsulation
        self._contact = contact

    @abstractmethod
    def display_info(self):
        pass

# ---------------- Subclasses ----------------
class Voter(Person):
    def _init_(self, name, contact, voter_id):
        super()._init_(name, contact)
        self.voter_id = voter_id
        self.has_voted = False

    def display_info(self):   # Polymorphism
        return f"Voter: {self._name}, ID: {self.voter_id}, Has Voted: {self.has_voted}"

class Candidate(Person):
    def _init_(self, name, contact, party):
        super()._init_(name, contact)
        self.party = party
        self.votes = 0

    def display_info(self):   # Polymorphism
        return f"Candidate: {self._name}, Party: {self.party}, Votes: {self.votes}"

# ---------------- Manager Class ----------------
class VotingSystem:
    total_votes = 0  # Class Attribute

    def _init_(self):
        self.voters = []
        self.candidates = []

    # ----- Register Voter -----
    def register_voter(self, voter):
        self.voters.append(voter)

    # ----- Register Candidate -----
    def register_candidate(self, candidate):
        self.candidates.append(candidate)

    # ----- Cast Vote -----
    def cast_vote(self, voter_id, candidate_name):
        voter = next((v for v in self.voters if v.voter_id == voter_id), None)
        candidate = next((c for c in self.candidates if c._name == candidate_name), None)

        if voter and candidate and not voter.has_voted:
            candidate.votes += 1
            voter.has_voted = True
            VotingSystem.total_votes += 1
            print(f"\n✅ Vote cast successfully by {voter._name} for {candidate._name} ({candidate.party})")
        else:
            print("\n❌ Vote not cast. Either voter not found, already voted, or candidate invalid.")

    # ----- Display Results -----
    def show_results(self):
        print("\n--- Election Results ---")
        for c in self.candidates:
            print(f"{c._name} ({c.party}) - {c.votes} votes")
        print(f"\nTotal Votes Cast: {VotingSystem.total_votes}")

    @classmethod
    def show_total_votes(cls):
        return f"Total Votes (system): {cls.total_votes}"

    @staticmethod
    def system_info():
        return "Welcome to Online Voting System 🗳"