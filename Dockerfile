FROM python:3.11.1-buster

WORKDIR /

# Install Git
RUN apt-get update && apt-get install -y git

# Install dependencies
RUN pip install runpod

# Clone the repository
RUN git clone https://github.com/MichaelSmithAI/testscripts.git /app

# Set the working directory
WORKDIR /app

# Install project dependencies
RUN pip install -r requirements.txt

# Set the entry point command
CMD [ "python", "-u", "/app/handler.py" ]
 