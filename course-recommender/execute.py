import subprocess

def execute_linux_command(command):

    try:
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        stdout = process.stdout
        stderr = process.stderr
        return_code = process.returncode

        return stdout, stderr, return_code

    except Exception as e:
        return None, str(e), -1


if __name__ == "__main__":
    command_to_execute = "python prompter.py && python extractor.py && python match.py"
    execute_linux_command(command_to_execute)
