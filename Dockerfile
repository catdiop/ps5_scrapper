FROM python:3.8-slim-buster

RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY . .

CMD ["python3", "main.py"]
