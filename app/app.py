from sanic import Sanic

from app.middlewares import middlewares
from app.listeners import listeners
from app.tasks import tasks
from app.routes import routes


class SanicServer(Sanic):
    def add_middlewares(self, middlewares_list):
        for middleware in middlewares_list:
            self.request_middleware.append(middleware)

    def add_listeners(self, listeners_list):
        for listener in listeners_list:
            self.register_listener(listener, event=listener.__name__)

    def add_tasks(self, tasks_list):
        for task in tasks_list:
            self.add_task(task)

    def add_routes(self, routes_list):
        for route in routes_list:
            self.add_route(route.view, route.url)

    def load_api(self):
        self.add_middlewares(middlewares)
        self.add_listeners(listeners)
        self.add_tasks(tasks)
        self.add_routes(routes)
