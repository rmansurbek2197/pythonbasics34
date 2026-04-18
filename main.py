class Voter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.voted = False

class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

class Election:
    def __init__(self):
        self.candidates = []
        self.voters = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def add_voter(self, voter):
        self.voters.append(voter)

    def vote(self, voter, candidate):
        if voter.voted:
            print("Voter already voted")
            return
        voter.voted = True
        candidate.votes += 1

    def show_results(self):
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

    def validate_voter(self, voter):
        if voter.age < 18:
            print("Voter is too young")
            return False
        return True

class OnlineVotingSystem:
    def __init__(self):
        self.election = Election()

    def start_election(self):
        while True:
            print("1. Add candidate")
            print("2. Add voter")
            print("3. Vote")
            print("4. Show results")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter candidate name: ")
                party = input("Enter candidate party: ")
                candidate = Candidate(name, party)
                self.election.add_candidate(candidate)
            elif choice == "2":
                name = input("Enter voter name: ")
                age = int(input("Enter voter age: "))
                voter = Voter(name, age)
                if self.election.validate_voter(voter):
                    self.election.add_voter(voter)
            elif choice == "3":
                name = input("Enter voter name: ")
                for voter in self.election.voters:
                    if voter.name == name:
                        candidate_name = input("Enter candidate name: ")
                        for candidate in self.election.candidates:
                            if candidate.name == candidate_name:
                                self.election.vote(voter, candidate)
                                break
                        break
            elif choice == "4":
                self.election.show_results()
            elif choice == "5":
                break
            else:
                print("Invalid choice")

online_voting_system = OnlineVotingSystem()
online_voting_system.start_election()