FROM python:3.8-slim
# Use the python latest image
COPY . ./
# Copy the current folder content into the docker image
RUN pip install flask gunicorn selenium
RUNdocker build -t <your name>/flask_uuid . apt-get install firefox-geckodriver
# Install the required packages of the application
CMD gunicorn --bind :$PORT app:app
# Bind the port and refer to the app.py app
