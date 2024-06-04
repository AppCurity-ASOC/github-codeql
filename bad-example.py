import sqlite3
import os

# SQL Injection vulnerability
def get_user_data(username):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    user_data = cursor.fetchall()
    connection.close()
    return user_data

# Command Injection vulnerability
def run_system_command(command):
    os.system(command)

# Hardcoded secret
def get_api_key():
    return "12345-ABCDE"

if __name__ == "__main__":
    # Example usage of SQL injection vulnerable function
    username = input("Enter username: ")
    print(get_user_data(username))

    # Example usage of command injection vulnerable function
    command = input("Enter command to run: ")
    run_system_command(command)

    # Example usage of hardcoded secret
    print("API Key:", get_api_key())

