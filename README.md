# AI-Text-to-Image-Generator
Develop a web application that converts text prompts into images using generative AI models like flux model

# Flux Schnell AI Image Generator

A **Flask** web application that generates AI images from text prompts using the **Flux Schnell** model on Nebius Studio. Enter your prompt, click generate, and view a gallery of your creations!

---

## 🔥 Features

* **Prompt-based image generation** with Flux Schnell (Nebius) via the OpenAI-compatible client
* **Dark-themed, responsive UI** with modern styling and hover animations
* **Gallery** to view all past generated images
* **Simple setup** — runs locally in VS Code
* **Environment variable support** for secure API key storage

## 🚀 Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/flux-schnell-image-generator.git
   cd flux-schnell-image-generator
   ```

2. **Create & activate a virtual environment**

   * On macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * On Windows (PowerShell):

     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   * Copy the example `.env.example` to `.env`:

     ```bash
     cp .env.example .env
     ```
   * Edit `.env` and add your Nebius API key:

     ```env
     NEBIUS_API_KEY=your_nebius_api_key_here
     ```

5. **Run the app**

   ```bash
   python app.py
   ```

6. **Open in browser**
   Visit `http://localhost:5000` to start generating images!

## 🗂️ Project Structure

```
flux-schnell-image-generator/
├── app.py                   # Flask application
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
├── templates/
│   └── index.html           # HTML template
├── static/
│   ├── css/
│   │   └── style.css        # Stylesheet
│   ├── js/
│   │   └── script.js        # Client-side JS
│   └── images/              # Generated images storage
└── README.md                # Project overview
```

## 📜 LICENSE

This project is licensed under the [MIT License](LICENSE).

---

*Made with ❤️ using Flask and Flux Schnell on Nebius Studio.*
