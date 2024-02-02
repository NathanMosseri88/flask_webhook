## Delegation and external webhooks for centralizing and automating tasks

Delegation takes in a request from the client, for each param sends a request
to an external webhook based on params, external webhook triggers task manager with params.
The webhook then send responses back through to the delegation server and then back to
the client

Client -> Delegation -> External -> Delegation -> Client

Things to work on: 

- Configure Ngrok wildcard domains and implement
  - Also set up security and restrictions like OAuth and/or IP restrictions
- Configure to listen on VM startup
- Write logic in external webhook to run tasks
- Set up protocol to send task logs (not webhook response) back to Delegation and Client
- Set up storage of task logs in delegation
- CI/CD (can be done through webhook route?)