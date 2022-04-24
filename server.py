#!/usr/bin/env python3

# server.py
#
# Currently, this server is pretty dumb - it just echos back whatever you send it.
#

import socket

# AF_INET: use IPv4 for addresses. To use IPv6, we'd set AF_INET6 instead.
# SOCK_STREAM: use TCP to send data. To use UDP, we'd set SOCK_DGRAM instead.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  port = 25000
  s.bind(("", port)) # Assign the socket to all network interfaces, on port 25000. ("" means any IP address, here)
  # The port number is arbitrary - but the client will need to know it in order to
  # connect to this server.
  #
  # Port numbers can be anything > 0 that fits in a 16-bit unsigned integer: [1,65535].
  #
  # Port numbers <1024 may be reserved for certain protocols, so avoid those.
  # (For example, SSH is port 22, HTTP is port 80, HTTPS is port 443)
  
  # Set up the socket for listening, use the default value for backlog (# of unaccepted connections before closure).
  s.listen()
  
  # Start listening for a connection from a client, wait until we get one. Once we get one, returns
  # a new socket that represents the connection with this client.
  print(f"Server online, listening for connections on port {port} ...")
  conn, addr = s.accept()
  with conn:
    print(f"Connected to client from {addr}")
    
    while True:
      # Receive up to 256 bytes (characters) from the client, (BLOCKS)
      data = conn.recv(256)
      
      # If the client has stopped sending stuff, exit the loop.
      if not data:
        break
      
      # Send the received data back to the client.
      print(f"Received message from client, echoing it back.")
      conn.sendall(data)
