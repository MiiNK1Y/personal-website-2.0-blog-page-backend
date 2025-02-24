FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "blog:create_app()"]
