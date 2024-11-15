import random
import string

def generate_password(length):
    """Generates a random password of fixed length."""
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_files(user_count, profile_name, shared_user, username_start_with, password_count):
    try:
        user_count = int(user_count)
        shared_user = int(shared_user)
        password_count = int(password_count)

        with open("mikrotik.rsc", "w") as rsc_file, open("user.txt", "w") as user_file:
            for i in range(1, user_count + 1):
                password = generate_password(password_count)
                username = f"{username_start_with}{i}"
                rsc_file.write(f"/user-manager user add name={username} password={password} shared-users={shared_user}\n")
                rsc_file.write(f"/user-manager user-profile add profile={profile_name} user={username}\n")
                user_file.write(f"User: {username}   --->  Password: {password}\n")

        print("Files created successfully!")
    except ValueError:
        print("Please enter valid inputs!")

if __name__ == "__main__":
    user_count = input("Enter User Count: ")
    profile_name = input("Enter Profile Name: ")
    shared_user = input("Enter Shared User: ")
    username_start_with = input("Enter Username Start With: ")
    password_count = input("Enter Password Count: ")

    create_files(user_count, profile_name, shared_user, username_start_with, password_count)
