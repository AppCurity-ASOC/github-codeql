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
        # Whitelist allowed commands (example: only allow 'ls', 'pwd', 'date')
        allowed_commands = ['ls', 'pwd', 'date', 'echo', 'cat']
        if cmd_parts and cmd_parts[0] in allowed_commands:
            subprocess.run(cmd_parts, shell=False, check=True)
        else:
            print(f"Command '{cmd_parts[0] if cmd_parts else command}' is not allowed")
    except Exception as e:
        print(f"Error executing command: {e}")

# Command Injection with subprocess
def run_subprocess_command_vulnerable(command):
    # Security fix: Use subprocess with shell=False and command list
    import shlex
    try:
        cmd_parts = shlex.split(command)
        # Whitelist allowed commands
        allowed_commands = ['ls', 'pwd', 'date', 'echo', 'cat']
        if cmd_parts and cmd_parts[0] in allowed_commands:
            subprocess.call(cmd_parts, shell=False)
        else:
            print(f"Command '{cmd_parts[0] if cmd_parts else command}' is not allowed")
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