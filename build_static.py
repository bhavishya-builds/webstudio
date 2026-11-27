
from pathlib import Path
from app import app

output = Path("public")
output.mkdir(exist_ok=True)

# Render the Flask template into ordinary HTML
with app.test_client() as client:
    response = client.get("/")

    if response.status_code != 200:
        raise RuntimeError("Website rendering failed")

    html = response.get_data(as_text=True)

# Use a relative CSS path for static hosting
html = html.replace(
    'href="/static/style.css"',
    'href="style.css"'
)

(output / "index.html").write_text(
    html,
    encoding="utf-8"
)

# Copy the stylesheet into the published folder
css = Path("static/style.css").read_text(
    encoding="utf-8"
)

(output / "style.css").write_text(
    css,
    encoding="utf-8"
)

print("WebStudio static website generated successfully!")
