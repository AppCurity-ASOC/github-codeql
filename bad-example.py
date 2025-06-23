import sqlite3
import os
import subprocess

# SQL Injection vulnerability
def get_user_data_vulnerable(username):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    # Security fix: Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user_data = cursor.fetchall()
    connection.close()
    return user_data

# Command Injection vulnerability
def run_system_command_vulnerable(command):
    # Security fix: Use subprocess with shell=False and validate/whitelist commands
    # Split command into list to avoid shell interpretation
    import shlex
    try:
        cmd_parts = shlex.split(command)
        # Whitelist allowed commands (example list - adjust based on requirements)
        allowed_commands = ['ls', 'pwd', 'date', 'echo', 'cat']
        if cmd_parts[0] not in allowed_commands:
            print(f"Command '{cmd_parts[0]}' not allowed")
            return
        subprocess.run(cmd_parts, shell=False, check=True)
    except Exception as e:
        print(f"Error executing command: {e}")

# Command Injection with subprocess
def run_subprocess_command_vulnerable(command):
    # Security fix: Use subprocess with shell=False and proper command parsing
    import shlex
    try:
        cmd_parts = shlex.split(command)
        # Whitelist allowed commands (example list - adjust based on requirements)
        allowed_commands = ['ls', 'pwd', 'date', 'echo', 'cat']
        if cmd_parts[0] not in allowed_commands:
            print(f"Command '{cmd_parts[0]}' not allowed")
            return
        subprocess.call(cmd_parts, shell=False)
    except Exception as e:
        print(f"Error executing command: {e}")

# Hardcoded secret
def get_api_key_vulnerable():
    # Security fix: Read API key from environment variable instead of hardcoding
    api_key = os.environ.get('API_KEY', 'default-key-for-development')
    return api_key

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