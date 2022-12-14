FROM python:3.9.16-alpine3.17
WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install translators
EXPOSE 5000
CMD ["flask", "run"]
 
