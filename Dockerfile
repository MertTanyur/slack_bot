# 
FROM python:3.9

# 
WORKDIR /code
RUN pip install fastapi uvicorn
# 
COPY ./requirements.txt /code/requirements.txt

COPY ./start.sh /start.sh
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
RUN chmod +x /start.sh
CMD ["./start.sh"]