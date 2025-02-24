import subprocess

def execute_linux_command(command):
    """
    Executes a command in the Linux terminal and returns the output.

    Args:
        command: The command to execute as a string.

    Returns:
        A tuple containing:
            - stdout (string): The standard output of the command.
            - stderr (string): The standard error of the command.
            - return_code (int): The exit code of the command.
    """
    try:
        process = subprocess.run(
            command,
            shell=True,  # Important for running shell commands
            capture_output=True,  # Capture stdout and stderr
            text=True,  # Decode output as text (UTF-8 by default)
            check=False  # Don't raise an exception if command fails (check return_code instead)
        )

        stdout = process.stdout
        stderr = process.stderr
        return_code = process.returncode

        return stdout, stderr, return_code

    except Exception as e:
        return None, str(e), -1  # Indicate an error occurred


if __name__ == "__main__":
    command_to_execute = "python prepare_input.py && python resume_scorer.py && python score_extractor.py"  # Example command: list files in /home directory

    execute_linux_command(command_to_execute)
