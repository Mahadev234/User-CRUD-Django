# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate
# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "user_crud.wsgi:application"]
