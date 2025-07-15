import os

r, w = os.pipe()

if os.fork() == 0:  # Child
    os.close(r)
    os.write(w, b"Hello")
    os.close(w)
else:  # Parent
    os.close(w)
    data = os.read(r, 100)
    print(f"Received: {data.decode()}")
    os.close(r)
