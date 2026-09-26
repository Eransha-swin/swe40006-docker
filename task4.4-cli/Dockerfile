FROM python:3.12-alpine
ENV PYTHONUNBUFFERED=1
RUN adduser -D appuser && mkdir /data && chown appuser /data
WORKDIR /app
COPY summarise.py .
USER appuser
VOLUME /data
ENTRYPOINT ["python", "summarise.py"]