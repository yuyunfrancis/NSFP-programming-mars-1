from __future__ import annotations

from .user import User
from typing import List


class UserManagement:
    """Main class to manage the user accounts

    Attributes:
        users: A list of users
        status_file: file where log ins are recorded
    """

    def __init__(self, status_file: str = 'data/.logged_in', users: List[User] = []) -> None:
        self.users = users
        self.status_file = status_file

    def get_logged_in_user(self) -> User:
        """Returns the logged in user
        """
        try:
            with open(self.status_file, 'r') as f:
                logged_in_username = f.read().strip()
                if not logged_in_username:
                    raise ValueError("No user is logged in.")
                return self.get_user_details(logged_in_username)
        except FileNotFoundError:
            raise ValueError("No user is logged in.")

    def get_user_details(self, username: str) -> User:
        """Returns the account of a user

        Args:
            username: the target username
        """
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError(f"No user with username '{username}' found.")

    @staticmethod
    def load(infile: str = 'data/credentials.txt') -> UserManagement:
        """Loads the accounts from a file"""
        with open(infile, 'r') as f:
            users = [User(elements[0], elements[3], elements[4], bool(elements[5])) for line in f.readlines() if
                     (elements := line.strip().split(':'))]
            return UserManagement(users=users)
