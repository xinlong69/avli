from pathlib import Path

for path in Path(".").glob("**/*.sh"):
    data = path.read_bytes()
    if b"\r\n" in data:
        path.write_bytes(data.replace(b"\r\n", b"\n"))
