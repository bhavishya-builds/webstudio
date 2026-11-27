from datetime import datetime
from urllib.parse import quote
from flask import Flask, render_template

app = Flask(__name__)

PROFILE_DATA = {
    "name": "Bhavishya",
    "brand": "bhavishya",
    "whatsapp_number": "918800821766",
    "whatsapp_message": "Hi Bhavishya, I saw your website and want to ask about getting a site made.",
    "hero_photo": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1200&q=80",
    "about_points": [
        {
            "icon": "fa-book-open",
            "title": "College student building on the side",
            "desc": "I'm a college student who enjoys making clean websites and helping people put their work or shop online without overcomplicating things."
        },
        {
            "icon": "fa-store",
            "title": "Made for local vendors & shops",
            "desc": "Plenty of neighborhood shops, cafes, clinics, and service providers run on word of mouth. A simple page helps people find you and message you directly."
        },
        {
            "icon": "fa-user-check",
            "title": "For anyone who wants a site",
            "desc": "Whether you run a small business, teach, freelance, or just want a personal page of your own, I keep the process straightforward."
        }
    ],
    "how_i_work": [
        {
            "step": "01",
            "title": "Quick chat on WhatsApp",
            "desc": "You share what you do, who your customers are, and what you want the page to say—no technical terms needed."
        },
        {
            "step": "02",
            "title": "Clean layout & adjustments",
            "desc": "I put together a readable, well-spaced page and tweak text, photos, and sections until it feels right for you."
        },
        {
            "step": "03",
            "title": "Ready to share with people",
            "desc": "You get a website that works smoothly on phones and laptops, with your WhatsApp link right where visitors need it."
        }
    ],
    "who_i_help": [
        "Local grocery & daily-need stores",
        "Cafes, bakeries & tiffin services",
        "Tutors, coaching & music classes",
        "Salons, studios & local clinics",
        "Freelancers & small service teams",
        "Anyone wanting a personal web page"
    ],
    "services": [
        {
            "icon": "fa-shop",
            "title": "Local vendor & shop sites",
            "desc": "Clear pages showing what you sell or offer, where you're located, and a direct button to chat on WhatsApp."
        },
        {
            "icon": "fa-file-lines",
            "title": "Personal & small business pages",
            "desc": "Straightforward websites for individuals, tutors, and small teams who want a clean place to share details."
        },
        {
            "icon": "fa-mobile-screen-button",
            "title": "Phone-friendly layouts",
            "desc": "Pages designed to read comfortably on mobile screens as well as laptops, without clutter or slow loading."
        }
    ],
    "examples": [
        {
            "tag": "Local shop",
            "title": "Neighborhood bakery & daily goods",
            "desc": "A simple menu and daily items page where nearby customers can see what's available and send an order message on WhatsApp.",
            "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1000&q=80",
            "notes": ["Mobile menu", "WhatsApp order link", "Hours & location"]
        },
        {
            "tag": "Individual & local service",
            "title": "Classes & local studio page",
            "desc": "A calm, easy-to-read page covering timings, what's offered, and quick contact details for people looking to reach out.",
            "image": "https://images.unsplash.com/photo-1488190211105-8b0e65b80b4e?auto=format&fit=crop&w=1000&q=80",
            "notes": ["Clear sections", "Easy contact", "Fast on phone"]
        },
        {
            "tag": "Cafe & food spot",
            "title": "Small cafe & takeaway menu",
            "desc": "Built for quick viewing on a customer's phone—highlights popular items, opening hours, and a direct tap to message or get directions.",
            "image": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1000&q=80",
            "notes": ["Quick item list", "Directions link", "Direct chat"]
        },
        {
            "tag": "Personal & freelance",
            "title": "Simple portfolio & inquiry page",
            "desc": "A clean single-page layout for someone who wants a tidy spot online to introduce themselves, show work, and take inquiries.",
            "image": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?auto=format&fit=crop&w=1000&q=80",
            "notes": ["Clean intro", "Work highlights", "WhatsApp CTA"]
        }
    ]
}


@app.route("/")
def home():
    encoded_msg = quote(PROFILE_DATA["whatsapp_message"])
    whatsapp_url = f"https://wa.me/{PROFILE_DATA['whatsapp_number']}?text={encoded_msg}"

    return render_template(
        "index.html",
        profile=PROFILE_DATA,
        whatsapp_url=whatsapp_url,
        current_year=datetime.now().year
    )


if __name__ == "__main__":
    app.run(debug=True)