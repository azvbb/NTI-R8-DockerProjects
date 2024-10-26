# Text Submission App Using Flask

This is a simple web application that allows users to submit text, which is then saved in a text file on the server. This project uses **Flask** for the backend, **HTML** and **CSS** for the frontend, and **Docker Compose** for easy deployment with separate containers for frontend and backend services.

After running the compose. Frontend and Backend containers will be up and then we can go to localhost:8080 and add any text we want and it will be saved to the text file "data.txt" in /backend/data directory. Data is presistent even after stopping the containers.

---

# Hostname Writing with Shared Volume

This project demonstrates how multiple Docker containers can interact through a shared volume. Each container writes its hostname to a shared volume, allowing data sharing between containers. One container lists the contents of the shared volume to display all hostnames written by other containers.

After running the compose. we can check the files created by checking container_3 logs. We find 2 txt files with the hostnames of the containers "their container IDs".
