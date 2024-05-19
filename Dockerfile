# Start your image with a node base image
FROM python:3.10-slim-buster
EXPOSE 8000

# The /app directory should act as the main application directory
WORKDIR /app

RUN apt-get update && apt-get install -y cron


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./source .
COPY cronjob /etc/cron.d/cronjob

RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

CMD ["cron","-f"]

#ENTRYPOINT ["./feed_parse.sh" ]






# CMD ["cron", "-f"]
#----

# RUN chmod +x /app/main.py



# RUN touch /var/log/linkedin-auto-post.log

# CMD ["cron", "-f"]