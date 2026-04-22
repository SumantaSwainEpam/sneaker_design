# 👟 AIR JORDAN — Sneaker World Room

> A premium, interactive sneaker showcase featuring the complete Air Jordan legacy — built with HTML, CSS, JavaScript, and served via Streamlit.

![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56+-ff4b4b?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🎨 **Premium Dark UI** — cinematic red-and-black design inspired by Jordan Brand aesthetics
- 👟 **20 Iconic Sneakers** — every legendary Air Jordan colorway from 1985 to 2024
- 🖼️ **Real Product Images** — AI-generated high-quality sneaker photos, embedded as base64 (fully self-contained)
- 🃏 **3D Hover Cards** — interactive tilt effect with smooth animations on each sneaker card
- 📜 **Scroll-triggered Animations** — cards fade in as you scroll down
- 🏷️ **Accurate Metadata** — correct model names, colorways, release years, and retail prices
- 🌐 **Shareable via Streamlit** — one-command deploy to Streamlit Community Cloud

---

## 🗂️ Project Structure

```
sneaker_design/
├── main.py          # Streamlit app — serves design.html with embedded images
├── design.html      # Core UI — pure HTML/CSS/JS sneaker showcase
├── images/          # AI-generated sneaker product photos
│   ├── aj1.png      # Air Jordan 1 (Chicago)
│   ├── aj3.png      # Air Jordan 3 (Fire Red)
│   ├── aj4.png      # Air Jordan 4 (Bred)
│   ├── aj5.png      # Air Jordan 5 (Grape)
│   ├── aj6.png      # Air Jordan 6 (Infrared)
│   └── aj11.png     # Air Jordan 11 (Concord)
├── pyproject.toml   # Project metadata and dependencies (uv)
└── README.md        # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- [`uv`](https://github.com/astral-sh/uv) package manager (recommended) **or** `pip`

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sneaker_design.git
cd sneaker_design
```

### 2. Install dependencies

**With `uv` (recommended):**
```bash
uv sync
```

**With `pip`:**
```bash
pip install streamlit
```

### 3. Run the app

**With `uv`:**
```bash
uv run streamlit run main.py
```

**With `streamlit` directly:**
```bash
streamlit run main.py
```

Then open **http://localhost:8501** in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud (Free)

Share with anyone in 3 steps:

1. Push this repo to GitHub
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub
3. Click **"New app"** → select your repo → set main file to `main.py` → **Deploy**

You'll get a permanent public URL like:
```
https://your-app-name.streamlit.app
```

---

## 🧱 Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Frontend  | HTML5, Vanilla CSS, JavaScript    |
| Server    | Python + Streamlit                |
| Packaging | `uv` / `pyproject.toml`           |
| Fonts     | Google Fonts (Bebas Neue, Barlow) |
| Images    | AI-generated product photography  |

---

## 👟 Sneaker Collection

| # | Model | Colorway | Year | Price |
|---|-------|----------|------|-------|
| 01 | Air Jordan 1 Retro High OG | Chicago | 1985 | $180 |
| 02 | Air Jordan 3 Retro | Fire Red | 1988 | $200 |
| 03 | Air Jordan 4 Retro | Bred | 1989 | $215 |
| 04 | Air Jordan 5 Retro | Grape | 1990 | $200 |
| 05 | Air Jordan 6 Retro | Infrared | 1991 | $200 |
| 06 | Air Jordan 11 Retro | Concord | 1995 | $225 |
| 07 | Air Jordan 12 Retro | Flu Game | 1997 | $200 |
| 08 | Air Jordan 13 Retro | He Got Game | 1998 | $210 |
| 09 | Air Jordan 14 Retro | Last Shot | 1999 | $195 |
| 10 | Air Jordan 1 Low OG | Royal Blue | 1985 | $140 |
| … | + 10 more modern retros | | | |

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

> **Disclaimer:** Air Jordan, Nike, and the Jumpman logo are trademarks of Nike, Inc. This project is fan-made and not affiliated with or endorsed by Nike, Inc.

---

## 🙌 Acknowledgements

- Inspired by the legacy of **Michael Jordan** and Jordan Brand
- UI design inspired by Nike's premium digital experiences
- Built with ❤️ using [Streamlit](https://streamlit.io)
