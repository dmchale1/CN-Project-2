# **Project 2: The Bulletin Board**
In this project, we implemented a client-server application that allows users to join groups, post messages to those groups, and see messages from others within the group.
The user inputs the address and port from the client, that client connects to the server, then the user can start chatting. The user can either post messages to the main board, or choose to join any number of active groups, all posts to which are kept separate from the main board. Only the previous two messages are shown to the user at a time, but previous messages can be accessed so long as the user knows the message ID. A user can join and leave as many groups as they wish at any time. When the user is finished on the board, they may exit the program entirely at any time.

## **Commands:**
The user has access to a number of commands:
1. The %connect command takes the address and port number as arguments, then attempts to connect the client to the server using those values
2. The %join command has the server attempt to add the user to the main board, then show them previous messages if successful
3. The %post command takes the content of the user message and posts it to the board
4. The %users command prints a list of all users to the user who invoked it
5. The %leave command removes the user's username from the username list, then prints a message to other users announcing the leave
6. The %message command takes a message ID supplied by the user in the command and attempts to locate the message with that ID in the message log, displaying it to the user if successful
7. The %exit command causes the client to disconnect from the server, then exit its program
8. The %group command displays a list of every active group to the user
9. The %groupjoin command takes either a group name or group ID as an argument, and will attempt to add the user to that group
10. The %grouppost command takes first the group name/id, then the message subject, and the message body as arguments, and will post the specified message to the specified group only.
11. The %goupusers command takes a group name/id as an argument and displays a list of all group members to the user
12. The %groupleave command takes a group name/id as an argument and removes the user from the group if they are in it
13. %groupmessage takes a group name/id and a message id as arguments, and displays the message in the group associated with that id to the user
14. %help displays a list of all group-related commands and what they do to the user for reference
