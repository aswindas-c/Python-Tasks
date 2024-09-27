import falcon
from waitress import serve

from FalconApp.controller.main_controller import MainController

app = falcon.App()

app.add_route('/users', MainController())
app.add_route('/users/{email}', MainController())

if __name__ == '__main__':
    print("Server is starting on http://127.0.0.1:8000")
    serve(app, host='localhost', port=8000)