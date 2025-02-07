from livereload import Server
server = Server()
server.watch('static/')
server.serve(port=8000)
