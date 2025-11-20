# SRE BEST PRACTICE: Use specific, slim base images

FROM python:3.9-slim



# Set working directory

WORKDIR /app



# Copy requirements first to leverage Docker Cache

COPY requirements.txt .



# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt



# Copy the rest of the application

COPY . .



# SRE BEST PRACTICE: Non-Root User

RUN useradd -m appuser

USER appuser



# Expose the port

EXPOSE 5000



# Define the command to run the app

CMD ["python", "app.py"]

