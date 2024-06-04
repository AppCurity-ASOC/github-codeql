import sqlite3
import os
import subprocess

# SQL Injection vulnerability
def get_user_data_vulnerable(username):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user_data = cursor.fetchall()
    connection.close()
    return user_data

# Command Injection vulnerability
def run_system_command_vulnerable(command):
    os.system(command)

# Command Injection with subprocess
def run_subprocess_command_vulnerable(command):
    subprocess.call(command, shell=True)

# Hardcoded secret
def get_api_key_vulnerable():
    return "12345-ABCDE"

if __name__ == "__main__":
    # Example usage of SQL injection vulnerable function
    username = input("Enter username: ")
    print(get_user_data_vulnerable(username))

    # Example usage of command injection vulnerable function
    command = input("Enter command to run: ")
    run_system_command_vulnerable(command)
    run_subprocess_command_vulnerable(command)

    # Example usage of hardcoded secret
    print("API Key:", get_api_key_vulnerable())

