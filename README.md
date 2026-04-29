# 🤖 Freezer AI — Asistente Virtual con Voz en Tiempo Real

Una página web interactiva donde podés hablarle o escribirle a **Freezer**, el Emperador del Universo de Dragon Ball Z. Responde en personaje usando IA y habla con su voz real gracias a síntesis de voz en tiempo real.


## ✨ Características

- 💬 Chat por texto o por voz (micrófono)
- 🗣️ Voz en tiempo real con Fish Audio
- 🧠 Respuestas generadas por Gemini AI en personaje
- 🌌 Interfaz animada con temática espacial

---

## 🛠️ Stack

- **Frontend:** HTML + CSS + JavaScript
- **Backend:** Python (proxy local)
- **APIs:** Google Gemini (texto) + Fish Audio (voz)

---

### . Configurá tus API Keys

**En `proxy_fishaudio.py`** reemplazá:

FISH_AUDIO_API_KEY = "tu_api_key_de_fish_audio"
FISH_AUDIO_VOICE_ID = "id_de_la_voz_en_fish_audio"


**En `freezer.html`** reemplazá:

const API_KEY = "tu_api_key_de_gemini";


### . Ejecutá el proxy de Python

** CMD/Terminal en la carpeta del proyecto:**
bash
cd ruta/a/la/carpeta
python proxy_fishaudio.py

Deberías ver:

Proxy corriendo en http://localhost:3001


> ⚠️ El proxy tiene que estar corriendo todo el tiempo que uses la app. No cierres la terminal.

### 4. Abrí el HTML

Abrí freezer.html con **Live Server** en VS Code (click derecho → Open with Live Server) o directamente desde el explorador de archivos.

---

## 🔑 Cómo conseguir las API Keys

### Gemini (Google)
1. Entrá a [aistudio.google.com](https://aistudio.google.com)
2. Get API Key → Create API Key
3. Pegala en `freezer.html`

### Fish Audio
1. Creá una cuenta en [fish.audio](https://fish.audio)
2. Settings → API Keys → Create
3. Para el Voice ID: buscá la voz que quieras, el ID está en la URL `fish.audio/m/ESTE-ES-EL-ID`
4. Pegá ambos en `proxy_fishaudio.py`

---

## 📁 Estructura del proyecto

```
freezer-ai/
├── freezer.html          # Frontend completo
├── proxy_fishaudio.py    # Proxy local para Fish Audio
└── freezerimage.png      # Imagen del personaje (opcional)

