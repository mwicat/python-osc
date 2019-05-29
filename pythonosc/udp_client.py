"""Client to send OSC datagrams to an OSC server via UDP."""

import socket


class UDPClient(object):
  """OSC client to send OscMessages or OscBundles via UDP."""

  def __init__(self, address, port, allow_broadcast):
    """Initialize the client.

    As this is UDP it will not actually make any attempt to connect to the
    given server at ip:port until the send() method is called.

    Args:
        address: IP address of server
        port: Port of server
        allow_broadcast: Allow for broadcast transmissions
    """
    self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self._sock.setblocking(0)
    if allow_broadcast:
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    self._address = address
    self._port = port

  def send(self, content):
    """Sends an OscBundle or OscMessage to the server."""
    self._sock.sendto(content.dgram, (self._address, self._port))
