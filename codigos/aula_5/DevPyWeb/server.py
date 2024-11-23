import http.server
import socketserver
import os
from urllib.parse import urlparse

# Configuração do servidor
PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do 'server.py'
VIEW_DIR = os.path.join(BASE_DIR, 'app', 'view')  # Caminho para 'app/view'
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')  # Caminho para 'public'

# Importar os controladores
from app.controller.MainController import MainController
from app.controller.ProductsController import ProductsController

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """
        Lida com as requisições GET e redireciona para o controlador.
        """
        path = urlparse(self.path).path

        # Roteamento das rotas principais
        if path == "/":
            self.route_to_controller(MainController.index())
        elif path == "/produtos":
            self.route_to_controller(ProductsController.index())
        else:
            super().do_GET()  # Caso o caminho não seja mapeado, o padrão é tentar servir o arquivo estático.

    def route_to_controller(self, view_name):
        """
        Redireciona para o controlador e renderiza a view correspondente.
        """
        # Verifica se o nome da view existe no diretório de views
        view_path = os.path.join(VIEW_DIR, view_name)
        if os.path.exists(view_path):
            with open(view_path, 'r') as view_file:
                content = view_file.read()

            # Envia a resposta com o conteúdo da view
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        else:
            self.send_error(404, "Página não encontrada")

# Inicializar o servidor
def run_server():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
