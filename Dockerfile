FROM python:3.11.6

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/ /app

# Expose the port that your FastAPI application will run on
EXPOSE 8000

# Command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
