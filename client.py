#!/usr/bin/env python3

# client.py
#
# Connects to the client, and sends some dummy text to it.
#

import sys
import argparse
import socket


# - - - - - - - - - - - - - - - #
# Parse command line arguments. #
# - - - - - - - - - - - - - - - #

parser = argparse.ArgumentParser(
  description="Send a message to the server at the given address and port.")

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
# (For example, SSH is port 22, HTTP is port 80, HTTPS is port 443)

parser.add_argument("-p","--port", default=25000, type=network_port,
                    help="port number to connect to, in range [1024,65535] (default: %(default)s)")

parser.add_argument("-s","--server", default="localhost",
                    help="IPv4 address or name of server to connect to (default: %(default)s)")

parser.add_argument("msg", metavar="...message...", default="Hey, anybody alive over there?", nargs="?",
                    help="message to send to the server (default: \'%(default)s\')")

args = parser.parse_args()



# - - - - - - - - - - - - - - - - - - - - - - #
# Send message to server and handle response. #
# - - - - - - - - - - - - - - - - - - - - - - #

# AF_INET: use IPv4 for addresses. To use IPv6, we'd set AF_INET6 instead.
# SOCK_STREAM: use TCP to send data. To use UDP, we'd set SOCK_DGRAM instead.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  # Attempt to connect to the server.
  s.connect((args.server, args.port))
  
  # Tell user what we're sending, then convert our message to a raw byte string.
  print(f"Sending message to {args.server}, port {args.port!r}:\n   \"{args.msg}\"")
  byte_msg = args.msg.encode(encoding="UTF-8")
  
  # If successful, send some text to the server.
  s.sendall(byte_msg)
  
  # Wait for the bytestring coming back from the server.
  data = s.recv(256)
  
  # Print out the received data so the user can see it.
  msg = data.decode(encoding="UTF-8")
  print(f"Received message from {args.server}, port {args.port!r}:\n   \"{msg}\"")
