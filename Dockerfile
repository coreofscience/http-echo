FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install -U pip && \
    pip install gunicorn falcon && \
    groupadd user && useradd -g user user
WORKDIR /app
ADD --chown=user:user echo.py /app/echo.py
USER user
CMD ["gunicorn", "-b", "0.0.0.0:8000", "echo:app()"]
