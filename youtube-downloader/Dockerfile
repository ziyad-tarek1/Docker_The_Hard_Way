FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN apt update -y && apt install -y ffmpeg
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]