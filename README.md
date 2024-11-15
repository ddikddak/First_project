# First_project

## Instructions to Run

Follow the steps below to clone the repository, configure, and run the Docker container for the project.

### 1. Clone the GitHub Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/ddikddak/First_project.git
```

### 2. Acces epository
```bash
cd First_project
```

### 3. Edit docker-compose.yml and put your openai api key
```docker-compose.yml
environment:
      - OPENAI_API_KEY=your-api-key
```

### 4. Build the docker container
```bash
      docker compose build
```
### 5. Run the docker container
```bash
      docker compose up
```
### 6. Acces the bot
```
      https://localhost:7860
```
