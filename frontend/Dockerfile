# Use an official Node runtime as a parent image
FROM node:23-alpine3.20

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json /app/

# Install app dependencies
RUN npm install

# Copy the current directory contents into the container
COPY . /app/

# Build the app
RUN npm run build

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable
ENV REACT_APP_API_SSL false
ENV REACT_APP_API_URL localhost:5000

# Run the app when the container launches
CMD [ "npm", "run", "start" ]
