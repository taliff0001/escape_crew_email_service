FROM python:3.12-slim

WORKDIR /escape_crew_email_service

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Command to run the application
CMD ["uvicorn", "escape_crew_email_service.main:app", "--host", "0.0.0.0", "--port", "8000"]