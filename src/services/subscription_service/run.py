from src.services.subscription_service.applications import Worker

if __name__ == '__main__':
    worker = Worker()
    worker.worker_run()
