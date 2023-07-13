# Start from the python:3.8 image
FROM python:3.8-alpine

# Use /usr/src/app as our workdir
WORKDIR /urs/src/app

# Copy all of the source code
COPY . .

# Set entrypoint
ENTRYPOINT ["python"]

# Add user called "appuser"
RUN adduser appuser \
    --disabled-password

# Change the user with the directive USER 
USER appuser

# Set command
CMD ["IUC.py"]
