# Text Submission App Using Flask

This is a simple web application that allows users to submit text, which is then saved in a text file on the server. This project uses **Flask** for the backend, **HTML** and **CSS** for the frontend, and **Docker Compose** for easy deployment with separate containers for frontend and backend services.

## Usage

After running `docker compose up`, the **Frontend** and **Backend** containers will be up and running. Follow these steps to use the application:

1. **Access the Application**:  
   Open your browser and go to [http://localhost:8080](http://localhost:8080).

2. **Add Text**:  
   On the main page, you can enter any text in the input box and click the "Send" button. The submitted text will be saved to a file named `data.txt` located in the backend's `/backend/data` directory.

3. **Persistent Data**:  
   The data in `data.txt` is stored on a Docker volume, so it remains available even if you stop and restart the containers. This ensures that your data persists between sessions.

-----------------------------------------------------------

# Hostname Writing with Shared Volume

This project demonstrates how multiple Docker containers can interact through a shared volume. Each container writes its hostname to a shared volume, allowing data sharing between containers. One container lists the contents of the shared volume to display all hostnames written by other containers.

## Usage

After running `docker compose up`, you can verify the files created in the shared volume by checking the logs of **container_3**.

1. **View Created Files**:  
   Check the logs of `container_3` by running:
   ```bash
   docker logs container_3
   ```

2. **Expected Output**:  
   You will find two `.txt` files named after the hostnames (container IDs) of `container_1` and `container_2`. These files are created in the shared `demo_volume`, making data accessible across containers.
