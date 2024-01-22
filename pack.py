from dog import Dog
class Pack:
    def __init__(self, Dog):
        self.leaderIndex = 0
        self.members = []

    def get_leader_name(self):
        return self.members[self.leaderIndex].get_name()

    def addMember(self, newMember: Dog):
        self.members.append(newMember)

    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(member.get_name())
pack