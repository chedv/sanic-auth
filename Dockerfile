# pull official base image
FROM python:3.8

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run the application
CMD ["python", "./main.py"]