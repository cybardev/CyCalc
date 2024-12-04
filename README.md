# CyCalc

## Multi-Container Docker Application with CI/CD: Calculator App Project

> [!NOTE]
> Complete Project Instructions: [DevOps Foundations Course/Project](https://github.com/shiftkey-labs/DevOps-Foundations-Course/tree/master/Project)

Submission by - [**Sheikh Saad Abdullah**](https://github.com/cybardev)

---

### Project Overview

**Project description:**

Calculator application with separate containers for frontend and backend, as an experiment to learn more about DevOps principles, containerization, various deployment options, and infrastructure-as-code.

**Files implemented:**

- [this README.md](./README.md)
  - provides context about the project and the learning experience gained from completing it
- [backend/Dockerfile](./backend/Dockerfile)
  - declarative configuration for the backend container image
- [frontend/Dockerfile](./frontend/Dockerfile)
  - declarative configuration for the frontend container image
- [docker-compose.yaml](./docker-compose.yaml)
  - declarative configuration for running the multi-container calculator application in development
- [render.yaml](./render.yaml) (Render Blueprint)
  - declarative configuration that defines the deployment infrastructure on as code
- [.github/workflows/github-actions.yml](./.github/workflows/github-actions.yml)
  - declarative configuration that defines the GitHub Actions workflow for running the CI/CD pipeline
- [.gitignore](./.gitignore)
  - configuration to ignore specific files and folders from version control (like editor configuration, cache files, etc.)
- [backend/requirements.txt](./backend/requirements.txt)
  - file generated through `pip freeze`, to specify required Python package dependencies for the backend
- [backend/test_app.py](./backend/test_app.py)
  - Python unit test script for the backend module
- [backend/gunicorn.config.py](./backend/gunicorn.conf.py)
  - gunicorn configuration script, allowing to specify API hostname and port via environment variables
- [frontend/src/App.js](./frontend/src/App.js)
  - [modified existing file] added trigonometric functions and power function to frontend, and changed `log` to `ln` to avoid confusion

### Docker Implementation

- **Backend Dockerfile** (Python API):
  - use a base Alpine Linux 3.20 image with Python 3.12 runtime set up
  - set working directory to an empty directory to isolate application from system files
  - copy application files from current directory into container image in the working directory set up in previous step
  - install required dependencies from `requirements.txt` using the `pip` package manager
  - indicate which port(s) are required to be exposed on the host network
  - specify default values for non-sensitive environment variables (hostname and port number in this case)
  - run the Flask application using `gunicorn` server

- **Frontend Dockerfile** (React App):
  - use a base Alpine Linux 3.20 image with Node JS 23 runtime set up
  - set working directory to an empty directory to isolate application from system files
  - copy package dependency specification files into container image
  - install required dependencies specified in aforementioned files using the `npm` package manager
  - copy application files from current directory into container image in the working directory set up in second step
  - build the React application by running the `build` script invoked by the `npm run` command
  - indicate which port(s) are required to be exposed on the host network
  - specify default values for non-sensitive environment variables (API hostname, API port number, and if SSL is enabled in the API in this case)
  - run the React application by running the `start` script invoked by the `npm run` command

- **Building and Distributing container images**:
  - Local development:
    - run following commands in the directories with the `Dockerfile`s
    - build: `docker build -t cycalc-frontend:latest .`
    - run: `docker run --name cycalc-frontend -p 3000:3000 cycalc-frontend:latest`
    - for backend, replace `frontend` in above commands with `backend`, and change ports from `3000:3000` to `5000:5000` (or `4000:5000` for macOS, since port 5000 is used by an OS component)
  - Distributing to container registries:
    - build and upload container images as GitHub Package to GitHub Container Registry automatically in GitHub Actions workflow

### Docker Compose YAML Configuration

- **Services:**
  - frontend: the React app, using the `frontend` directory as build context, served over the 3000 port on the local host network. Depends on the backend service. Uses an environment variable to specify which port the backend service is exposed on
  - backend: the Flask API, using the `backend` directory as build context, served over the 4000 port on the local host network
- **Networking:**
  - uses the default bridge network to have isolation between containers but has specified ports exposed so containers can communicate over the local host network
- **Environment Variables:**
  - for the frontend, I used an environment variable (`REACT_APP_API_PORT`) to specify what the port number of the Flask backend API would be
  - I did this because the default 5000 port on my host is occupied by an OS component (on macOS)

### CI/CD Pipeline (YAML Configuration)

- triggers:
  - on push or merged pull requests on the main branch, but only if Python (`*.py`) or JavaScript (`*.js`) files change
  - manually run from the GitHub Actions interface (website or hooks, like the VS Code extension)
- stages:
  - frontend and backend parallel build and test stages (one for each)
  - stage to build container image and push to GitHub Container Registry using official workflow
  - stage to deploy built images on Render via URL web hooks

### Lessons Learned

- port 5000 is occupied by a component of macOS (Control Center)
- React only reads environment variables prefixed with `REACT_APP_`, to avoid leaking sensitive data from the environment
- learned how Docker Compose works and how it can be used to set up a smooth development experience for multi-container applications
- learned multi-container app deployment on Render via their infrastructure-as-code (IaC) model - Render Blueprints. It was interesting to note the similarities between this and Docker Compose
- learned how to deploy to Render using web hooks from CI/CD pipelines, keeping the hook URL hidden as a repository secret
- connected custom domain to frontend application in Render: [calc.cybar.dev](https://calc.cybar.dev)

### Future Improvements

- add testing steps in Dockerfile to prevent building bad images
- optimize Docker images by leveraging multi-stage builds, distroless runtime images, compression software, etc.
- split CI/CD pipeline into multiple files (test, push to registry, deploy, etc.) for readability, modularity, and separation of concerns
- add functions and mathematical constants to calculator app frontend: variable base logarithms, _e_, _π_, _i_

---

### Credits

- This repository is a continuation of the work done in the [Project](https://github.com/cybardev/ShiftKey-DevOps/tree/master/Project) directory on this repo: [cybardev/ShiftKey-DevOps](https://github.com/cybardev/ShiftKey-DevOps)
- The aforementioned repository itself is a fork of the ShiftKey Labs repository: [shiftkey-labs/DevOps-Foundations-Course](https://github.com/shiftkey-labs/DevOps-Foundations-Course)
- Thanks to [Zainuddin Saiyed](https://github.com/Zain-Saiyed) for teaching the course and guiding us through DevOps, containerization, CI/CD, and relevant concepts.
- Thanks to [ShiftKey](https://shiftkeylabs.ca/) for hosting the certification program on a topic I'm deeply interested in.
