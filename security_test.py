
import subprocess

def get_user_profile(user_id):
    result = subprocess.run(
        ["echo", user_id],
        shell=False,
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout
