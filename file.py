
import subprocess

def get_user_profile(user_id):
    # Intentionally insecure for scanner testing:
    # user input is passed to a shell command.
    command = "echo " + user_id
    return subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    ).stdout
