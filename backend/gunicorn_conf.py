from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/ubuntu/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
#worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/log/access_log'
errorlog =  '/home/ubuntu/log/error_log'
capture_output = True
enable_stdio_inheritance = True
