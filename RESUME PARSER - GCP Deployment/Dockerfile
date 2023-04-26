FROM python:3.7

WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
ADD ./model ./model
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]