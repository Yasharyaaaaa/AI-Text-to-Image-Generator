import os
import base64
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv
from openai import OpenAI

# Load Nebius API key from .env
load_dotenv()
NEBIUS_KEY = os.getenv("NEBIUS_API_KEY")
if not NEBIUS_KEY:
    raise ValueError("Please set NEBIUS_API_KEY in your .env file")

# Initialize OpenAI client pointing to Nebius Studio
client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=NEBIUS_KEY
)

app = Flask(__name__)

# Ensure the images folder exists
images_dir = os.path.join(app.static_folder, "images")
os.makedirs(images_dir, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    new_image_url = None
    prompt_text = ""

    if request.method == "POST":
        prompt_text = request.form.get("prompt", "").strip()
        if prompt_text:
            try:
                # Generate image with Flux Schnell model on Nebius
                resp = client.images.generate(
                    model="black-forest-labs/flux-schnell",
                    prompt=prompt_text,
                    response_format="b64_json",
                    extra_body={
                        "response_extension": "png",
                        "width": 1024,
                        "height": 1024,
                        "num_inference_steps": 4,
                        "negative_prompt": "",
                        "seed": -1,
                        "loras": None
                    }
                )
                # Extract base64 PNG from the response
                b64 = resp.data[0].b64_json
                img_bytes = base64.b64decode(b64)

                # Save to static/images with a unique filename
                idx = len(os.listdir(images_dir)) + 1
                filename = f"{idx}.png"
                path = os.path.join(images_dir, filename)
                with open(path, "wb") as f:
                    f.write(img_bytes)

                # URL to display in the template
                new_image_url = url_for("static", filename=f"images/{filename}")

            except Exception as e:
                return f"Error generating image: {str(e)}", 500

    # Build gallery (newest first)
    files = sorted(os.listdir(images_dir), reverse=True)
    gallery = [url_for("static", filename=f"images/{fn}") for fn in files]

    return render_template(
        "index.html",
        prompt=prompt_text,
        new_image=new_image_url,
        gallery=gallery
    )

if __name__ == "__main__":
    app.run(debug=True)

       
    
    
              