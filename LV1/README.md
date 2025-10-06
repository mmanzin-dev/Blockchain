# Running TCP and UDP Echo Servers in Python

This guide describes how to start the TCP and UDP echo server scripts and send messages to them using corresponding client scripts.

## Running the TCP Echo Server

To start the TCP echo server, open your terminal and execute:

`python TCP_EchoServer.py`

The server will begin listening for incoming TCP connections on the specified localhost IP and port.

## Sending Data to the TCP Server

To send data to the TCP echo server, run the client script in another terminal:

`python TCP_EchoClient.py`

The client will connect to the server, send a message, and print the echoed response.

---

## Running the UDP Echo Server

To start the UDP echo server, open your terminal and execute:

`python UDP_EchoServer.py`

The server will begin listening for incoming UDP datagrams on the specified localhost IP and port.

## Sending Datagrams to the UDP Server

To send a datagram to the UDP echo server, run the client script in another terminal:

`python UDP_EchoClient.py`

The client will send a datagram to the server, receive an echo, and print the response.

---

**Note:** 
- Make sure that both server and client scripts are in the same directory or provide their full paths.
- Use **separate** terminal instances for running server and client scripts.
