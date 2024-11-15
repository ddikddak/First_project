# First_project

#Instructions to run

1. Clone the github repo using
git clone https://github.com/ddikddak/First_project.git

2. Acces repositorie
cd First_project

3. Edit docker-compose.yml and put your openai api key
environment:
      - OPENAI_API_KEY=your-api-key

4. Build the docker container
docker compose build

5. Run the docker container
docker compose up

6. Acces the bot
https://localhost:7860
