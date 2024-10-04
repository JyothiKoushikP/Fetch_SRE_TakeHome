FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements.txt first to take advantage of Docker caching
COPY requirements.txt /app/

# Step 4: Install the required Python packages from requirements.txt (Using pip Python manager)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application files into the container
COPY . /app/

# Step 6: Set an environment variable (This sets for the INPUT_FILE which will be taken in the code for processing)
ENV INPUT_FILE=Input.yml

# Step 7: Define the default command to run the main.py file
CMD ["python3", "main.py"]
