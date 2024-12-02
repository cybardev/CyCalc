# CyCalc

## Multi-Container Docker Application with CI/CD: Calculator App Project

> [!NOTE]
> Complete Project Instructions: [DevOps Foundations Course/Project](https://github.com/shiftkey-labs/DevOps-Foundations-Course/tree/master/Project)

Submission by - [**Sheikh Saad Abdullah**](https://github.com/cybardev)

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

**Explain your Dockerfiles:**

- **Backend Dockerfile** (Python API):
  - Here please explain the `Dockerfile` created for the Python Backend API.
  - This can be a simple explanation which serves as a reference guide, or revision to you when read back the readme in future.

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

- **Frontend Dockerfile** (React App):
  - Similar to the above section, please explain the Dockerfile created for the React Frontend Web Application.

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

**Use this section to document your choices and steps for building the Docker images.**

### Docker Compose YAML Configuration

**Break down your `docker-compose.yml` file:**

- **Services:** List the services defined. What do they represent?
- **Networking:** How do the services communicate with each other?
- **Volumes:** Did you use any volume mounts for persistent data?
- **Environment Variables:** Did you define any environment variables for configuration?

**Use this section to explain how your services interact and are configured within `docker-compose.yml`.**

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

### CI/CD Pipeline (YAML Configuration)

**Explain your CI/CD pipeline:**

- What triggers the pipeline (e.g., push to main branch)?
- What are the different stages (build, test, deploy)?
- How are Docker images built and pushed to a registry (if applicable)?

**Use this section to document your automated build and deployment process.**

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

### Assumptions

- List any assumptions you made while creating the Dockerfiles, `docker-compose.yml`, or CI/CD pipeline.

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

### Lessons Learned

- What challenges did you encounter while working with Docker and CI/CD?
- What did you learn about containerization and automation?

**Use this section to reflect on your experience and learnings when implementing this project.**

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->

### Future Improvements

- How could you improve your Dockerfiles, `docker-compose.yml`, or CI/CD pipeline?
- (Optional-Just for personal reflection) Are there any additional functionalities you would like to consider for the calculator application to crate more stages in the CI/CD pipeline or add additional configuration in the Dockerfiles?

**Use this section to brainstorm ways to enhance your project.**

<!-- Include explanation here -->
<!-- NOTE: It is not compulsory to include detailed explanations, writing succint concise points would also sufice. Make sure maintain readability and clarity. -->
