import subprocess

try:
    result = subprocess.run(
        ["ipconfig"],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Exit code:", e.returncode)
    print("STDOUT:")
    print(e.stdout)
    print("STDERR:")
    print(e.stderr)
