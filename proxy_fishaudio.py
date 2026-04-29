import json
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler

#Aquí se colocan las API de fish audio que se usó y la de la voz en específico

FISH_AUDIO_API_KEY = "Api_Fish_General"
FISH_AUDIO_VOICE_ID = "ID_Voz_Específica"



PUERTO = 3001


class ProxyHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/tts":
            self.send_response(404)
            self.end_headers()
            return

        try:
            largo = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(largo))
            texto = body.get("text", "")

            print(f"  Generando audio: {texto[:60]}...")

            payload = json.dumps({
                "text": texto,
                "reference_id": FISH_AUDIO_VOICE_ID,
                "format": "mp3",
                "latency": "normal"
            }).encode()

            req = urllib.request.Request(
                "https://api.fish.audio/v1/tts",
                data=payload,
                headers={
                    "Authorization": f"Bearer {FISH_AUDIO_API_KEY}",
                    "Content-Type": "application/json",
                    "model": "s2"
                },
                method="POST"
            )

            with urllib.request.urlopen(req, timeout=30) as resp:
                audio = resp.read()

            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "audio/mpeg")
            self.send_header("Content-Length", str(len(audio)))
            self.end_headers()
            self.wfile.write(audio)
            print(f"  Audio enviado ({len(audio)} bytes)")

        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            print(f"  Fish Audio ERROR {e.code}: {error_body}")
            self.send_response(e.code)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(error_body.encode())

        except Exception as e:
            print(f"  ERROR: {e}")
            self.send_response(500)
            self._cors()
            self.end_headers()
            self.wfile.write(str(e).encode())

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    if "TU_API_KEY" in FISH_AUDIO_API_KEY:
        print("Pega tu API Key en FISH_AUDIO_API_KEY")
        exit(1)
    if "PEGA_EL_ID" in FISH_AUDIO_VOICE_ID:
        print("Pega el ID de la voz en FISH_AUDIO_VOICE_ID")
        exit(1)

    server = HTTPServer(("localhost", PUERTO), ProxyHandler)
    print(f"Proxy corriendo en http://localhost:{PUERTO}")
    print(f"Ctrl+C para detener.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nProxy detenido.")
