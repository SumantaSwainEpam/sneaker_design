import streamlit as st
import streamlit.components.v1 as components
import base64
import re
from pathlib import Path

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AIR JORDAN — Sneaker World Room",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── HIDE STREAMLIT DEFAULT UI FOR FULL IMMERSION ──────────────────────────
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .stMainBlockContainer {
        padding: 0 !important;
    }
    iframe {
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─── HELPERS ───────────────────────────────────────────────────────────────

def image_to_base64(image_path: Path) -> str:
    """Convert an image file to a base64 data URI."""
    suffix = image_path.suffix.lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif"}
    mime = mime_map.get(suffix, "image/png")
    data = image_path.read_bytes()
    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def embed_images_in_html(html_content: str, base_dir: Path) -> str:
    """Replace all image path references with inline base64 data URIs.
    Handles both HTML src attributes AND JavaScript string literals.
    This makes the HTML fully self-contained so it works inside an iframe srcdoc.
    """

    def replace_path(match):
        img_path_str = match.group(1)
        img_path = base_dir / img_path_str
        if img_path.exists():
            data_uri = image_to_base64(img_path)
            return match.group(0).replace(img_path_str, data_uri)
        return match.group(0)  # leave unchanged if file not found

    # Match any occurrence of images/something.ext in quotes (single or double)
    pattern = r"""['"]?(images/[^"'\s,]+)['"]?"""
    return re.sub(pattern, replace_path, html_content)


# ─── MAIN ──────────────────────────────────────────────────────────────────

def main():
    base_dir = Path(__file__).parent
    html_file = base_dir / "design.html"

    if not html_file.exists():
        st.error("❌ `design.html` not found! Make sure it's in the same directory as `main.py`.")
        return

    # Read the HTML and inline all images as base64
    raw_html = html_file.read_text(encoding="utf-8")
    self_contained_html = embed_images_in_html(raw_html, base_dir)

    # Render via components.html (full-width, scrollable)
    components.html(self_contained_html, height=3000, scrolling=True)


if __name__ == "__main__":
    main()
