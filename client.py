import socket
import threading

# Create the client socket as well as a counter variable
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
checker = 0

# Check for messages until the checker variable is iterated
while checker == 0:
    try:
        # Get a message from the user, then send it to the server
        message = input()

        # Look for the "%connect" message to be entered
        if message == "%connect":
            # Get host and port numbers from the user
            address = input("Enter Address: ")
            port = input("Enter the port number: ")
            port = int(port)

            # Connect to the server with the client socket
            client_socket.connect((address, port))

            # Send a user-specified username to the server
            user = input("Enter username: ")
            client_socket.send(user.encode())

            # Now that the user is connected, iterate the checker so the program can move on
            checker += 1
    except:
        # If there is an error connecting to the server, exit the program
        print("Error connecting to the server")
        client_socket.close()
        exit()

# Function to send messages input by the user
def send():

    # Continuously check for messages to send to the server
    while 1:
        try:
            # Get a message from the user, then send it to the server
            message = input()
            client_socket.send(message.encode())
        
            # If the user typed "exit", close the connection to the server
            if message == "%exit":
                print("Exiting the server")
                client_socket.close()
                exit()
        except:
            # Exit the program if there's an error sending a message
            print("Error sending a message")
            client_socket.close()
            exit()

# Start a thread to run the send() function
send_thread = threading.Thread(target=send)
send_thread.start()

# In the main thread, continuously listen for previous messages from the server
while 1:
    try:
        # Receive and print out a message from the server
        message = client_socket.recv(1024).decode()
        print(message)

    except:
        # Exit the program if there's an error while getting a message
        print("Error obtaining a message")
        client_socket.close()
        exit()