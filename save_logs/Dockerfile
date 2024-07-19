FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY telegram_zakupki_handler /code/
COPY telegram_zakupki_handler/manage.py /code/
COPY telegram_zakupki_handler/wait-for-it.sh /code/

# Ensure wait-for-it.sh is executable
RUN chmod +x /code/wait-for-it.sh

# Specify the command to run on container start
CMD ["/code/wait-for-it.sh", "pgdb_save_logs:5433", "--", "sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
