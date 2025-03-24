import http.server
import socketserver
import threading
import webbrowser
import folium

from config import PORT, CITY_ALMATY


m = folium.Map(location=CITY_ALMATY, zoom_start=12)

m.save('almaty.html')

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Сервер запущен на http://localhost:{PORT}")
        httpd.serve_forever()

thread = threading.Thread(target=start_server, daemon=True)
thread.start()

webbrowser.open(f"http://localhost:{PORT}/almaty.html")

try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nСервер остановлен")