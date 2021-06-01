FROM python:3.9.2-slim-buster

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy default configuration
COPY ./config/config-default.json ./config

# Bundle app source
COPY . .

CMD ["python3","-u","./main.py"]