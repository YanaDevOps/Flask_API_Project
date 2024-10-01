# Flask_API_Project

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)

## 📋 Description
Flask_API_Project is a simple RESTful API server built with Flask, designed to demonstrate a basic setup for creating and running RESTful services inside a Docker container. This project includes multiple routes for testing and learning API development.

## 🚀 Start of work

### 1. Prerequisites
- Python: 3.8 or later
- Docker: Installed and configured

### 2. Installation
1. Clone the repository:
```bash
git clone https://github.com/YanaDevOps/Flask_API_Project.git
cd Flask_API_Project
```

2. Install dependencies locally:
```bash
pip install -r requirements.txt
```

3. Run the application locally:
```bash
python app.py
```

4. Open the app in your browser:
```bash
http://localhost:5000
```

## Running the Application in Docker
1. Build the Docker image:
```bash
docker build -t flask_api_project:1.0.0 .
```

2. Run the container:
```bash
docker run -d -p 8080:5000 --name flask_api_project flask_api_project:1.0.0
```

3. Open the app in your browser:
```bash
http://localhost:8080
```

## Project Structure
```
Flask_API_Project/
├── Dockerfile          # Docker configuration for multi-stage builds
├── app.py              # Flask application with multiple routes
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

### Features
- /: Main route returning a welcome message.
- /status: Returns server status in JSON format.
- /data: Accepts POST requests and returns received data.

### Technologies Used
- Python 3.8
- Flask 2.2.0
- Docker

### Author
Name: Yana Lysenko

GitHub: [YanaDevOps](https://github.com/YanaDevOps)
