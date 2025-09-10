import subprocess

# Define the system command to execute
command = ["ls", "-l"]  # Example: List files with details

# Execute the command and capture its output
# capture_output=True captures stdout and stderr
# text=True decodes the output as a string (otherwise it's bytes)
result = subprocess.run(command, capture_output=True, text=True, check=True)

# Access the standard output from the command
command_output = result.stdout

# Print the captured output
print(command_output)
