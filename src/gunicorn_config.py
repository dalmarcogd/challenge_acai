from database import migration
from settings import PORT, HOST

bind = f"{HOST}:{PORT}"
workers = 2
max_requests = 100
max_requests_jitter = 5
keepalive = 120
timeout = 120
worker_class = "uvicorn.workers.UvicornWorker"

migration.upgrade()
