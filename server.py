#!/usr/bin/env python3

# server.py
#
# Currently, this server is pretty dumb - it just echos back whatever you send it.
#

import sys
import argparse
import socket


# - - - - - - - - - - - - - - - #
# Parse command line arguments. #

parser = argparse.ArgumentParser(
  description="Start the demo server, listen for clients on the given port.")

def network_port(net_port):
  p = int(net_port)
  if p < 1024 or p > 65535:
    raise argparse.ArgumentTypeError(f"Can't use port {p}, please use a port between 1024 and 65535")
  return p
# The port number is arbitrary - but the client will need to know it in order to
# connect to this server.
#
# Port numbers can be anything > 0 that fits in a 16-bit unsigned integer: [1,65535].
#
# Port numbers below 1024 may be reserved for certain protocols, so avoid those.
# (Ex: SSH is port 22, HTTP is port 80, HTTPS is port 443)

parser.add_argument("-p","--port", default=25000, type=network_port,
                    help="port number to listen on, in range [1024,65535] (defaults to 25000)")

args = parser.parse_args()



# - - - - - - - - - - - - - - - - - - - - #
# Listen for client and process messages. #

# AF_INET: use IPv4 for addresses. To use IPv6, we'd set AF_INET6 instead.
# SOCK_STREAM: use TCP to send data. To use UDP, we'd set SOCK_DGRAM instead.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(("", args.port)) # Assign the socket to all network interfaces, on the given port. ("" means any IP address, here)
  
  # Set up the socket for listening, use the default value for backlog (# of unaccepted connections before closure).
  s.listen()
  
  # Start listening for a connection from a client, wait until we get one. Once we get one, returns
  # a new socket that represents the connection with this client.
  print(f"Server online, listening for connections on port {args.port} ...")
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
