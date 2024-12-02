import os

bind = f"{os.environ.get("API_HOST", "0.0.0.0")}:{os.environ.get("API_PORT", "5000")}"
