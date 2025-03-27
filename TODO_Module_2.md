# ✅ To-Do-Liste für `helab_phase3_Module_2`

## 🔧 Setup & Grundstruktur
- [ ] Neues Projektverzeichnis `helab_phase3_Module_2` anlegen
- [ ] Python-Virtualenv einrichten (`python -m venv venv`)
- [ ] Abhängigkeiten installieren:
  - Flask
  - colormath
  - numpy
- [ ] `requirements.txt` erzeugen
- [ ] Git-Repo initialisieren oder mit GitHub verknüpfen
- [ ] Heroku-App vorbereiten (neues Deployment oder Ziel definieren)

---

## 🧩 Funktionen & Erweiterungen

### 💡 Matching erweitern
- [ ] ΔE2000-Threshold konfigurierbar machen
- [ ] Mehrfach-Matching unterstützen (z. B. gegen mehrere LAB-Werte)
- [ ] Vorschau der Trefferfarben anzeigen (RGB, Hex)

### 💡 Usability verbessern
- [ ] Color Picker integrieren (HTML5/JS)
- [ ] Clientseitige Validierung der L*a*b*-Werte
- [ ] Nutzer-Feedback bei ungültigen Eingaben (z. B. Flash-Meldung)

### 💡 API ausbauen
- [ ] `/api/match` → JSON-Antwort mit Matching-Ergebnissen
- [ ] `/api/colors` → Liste aller gespeicherten Farben
- [ ] `/api/lab-to-rgb` mit Farb-Preview verbessern

---

## 🔐 Code-Qualität & Sicherheit
- [ ] Entferne deprecated Monkey-Patches (`asscalar`)
- [ ] Strukturiere `modules/` (z. B. `matching.py`, `color_tools.py`, `api.py`)
- [ ] Fehlerbehandlung & Logging konsolidieren
- [ ] CSRF-Schutz (z. B. mit Flask-WTF)

---

## 🌍 Deployment & Versionskontrolle
- [ ] GitHub-Repo für Modul 2 anlegen oder forken
- [ ] `Procfile` und `runtime.txt` für Heroku bereitstellen
- [ ] Git-Workflow einrichten (`git add/commit/push`)
- [ ] Heroku-Deploy testen und Log überprüfen

---

## ✨ Optional
- [ ] Suchverlauf anzeigen (Session oder persistent)
- [ ] Farbvergleichs-Chart als Visualisierung (Matplotlib / JS)
- [ ] Export der Ergebnisse (z. B. CSV/JSON)
