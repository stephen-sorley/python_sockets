# Python Sockets Example Project
Basic client/server sockets example using Python, intended for teaching and my own edification.

# Installation Instructions (Ubuntu Linux)
  - Install Git and Python 3.6 or newer if they're not already available: `sudo apt install git python3`
  - Download the project to your local machine: `git clone https://github.com/stephen-sorley/python_sockets.git`

# Run Instructions (Ubuntu Linux)
  - Open two terminal windows, then move into the `python_sockets` directory in both.
  - Run `./server.py` in one terminal window, then run `./client.py` in the other.
  - The client and server both use localhost (`127.0.0.1`) and the same port by default.

# Notes
  - The port and/or host address can be changed by passing optional arguments when you run the client or server. Run `./client.py --help` or `./server.py --help` for details.
  - If the client or server gets stuck waiting for a response, you can use `CTRL-C` at any time to force-kill the program.

# Resources
  - Tutorial on socket programming with Python: https://realpython.com/python-sockets/
  - Python3 'socket' module API docs: https://docs.python.org/3/library/socket.html
  - Official HOWTO for sockets: https://docs.python.org/3/howto/sockets.html


