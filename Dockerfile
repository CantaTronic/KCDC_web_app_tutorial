FROM python:3.7
EXPOSE 8344
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r requirements.txt
CMD streamlit run app.py --server.port 8344
