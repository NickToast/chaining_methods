class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member!")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

#Method to decrease the user's point's by amount specified
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("You do not have enough points!")
            return False
        else:
            self.gold_card_points = self.gold_card_points - amount
            return self

user_1 = User("Nick", "Tangsouvanh", "nt@gmail.com", 26)
user_2 = User("Joseph", "Apple", "Japple@gmail.com", 24)
user_3 = User("Mango", "Peach", "mangopeach@gmail.com", 21)

# user_1.display_info()

# user_1.enroll()
# user_1.display_info()

# user_1.spend_points(50)
# # print(user_1.gold_card_points)

# user_2.enroll()
# # print(user_2.gold_card_points)
# user_2.spend_points(80)

# user_1.display_info()
# user_2.display_info()
# user_3.display_info()

# user_1.enroll()

# user_3.spend_points(40)

user_1.display_info()
user_1.enroll().spend_points(50)
user_1.display_info()
user_2.enroll().spend_points(80)
user_2.display_info()
user_3.display_info()

# user_1.display_info().enroll().spend_points(50).display_info()
# user_2.enroll().spend_points(80).display_info()
