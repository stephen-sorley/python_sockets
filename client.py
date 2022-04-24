#!/usr/bin/env python3

# client.py
#
# Connects to the client, and sends some dummy text to it.
#

import socket

# AF_INET: use IPv4 for addresses. To use IPv6, we'd set AF_INET6 instead.
# SOCK_STREAM: use TCP to send data. To use UDP, we'd set SOCK_DGRAM instead.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # Specify what server we're connecting to (host name or address, and port),
  # and what message we're going to send.
  host = "localhost"
  port = 25000
  msg  = "Hey, anybody alive over there?"
  
  # Attempt to connect to the server.
  s.connect((host, port))
  
  # Tell user what we're sending, then convert our message to a raw byte string.
  print(f"Sending message to {host}, port {port!r}:\n   \"{msg}\"")
  byte_msg = msg.encode(encoding="UTF-8")
  
  # If successful, send some text to the server.
  s.sendall(byte_msg)
  
  # Wait for the bytestring coming back from the server.
  data = s.recv(256)
  
  # Print out the received data so the user can see it.
  print(f"Received message from {host}, port {port!r}:\n   \"{msg}\"")
