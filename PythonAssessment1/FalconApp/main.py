import falcon
from waitress import serve

from FalconApp.routes.post_route import PostRoute
from FalconApp.routes.get_route import GetRoute

app = falcon.App()

post_api = PostRoute()
get_api = GetRoute()

app.add_route('/users', post_api)
app.add_route('/users/{email}', get_api)

if __name__ == '__main__':
    print("Server is starting on http://127.0.0.1:8000")
    serve(app, host='localhost', port=8000)