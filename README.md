# Bhavishya — Web Developer & College Builder

> Bringing local businesses and big ideas online—one website at a time.

A responsive portfolio website built with **Python (Flask)**, **HTML5**, and **CSS3** for a college student creating clean, practical websites for local vendors, small shops, and individuals—complete with direct WhatsApp inquiry links.

---

## Overview

Many local shops, neighborhood vendors, tutors, and small businesses rely heavily on word-of-mouth and everyday messaging rather than complex web portals. This project presents a focused, easy-to-browse site where visitors can quickly understand who is building the site, what kinds of pages are offered, and how to start a conversation on WhatsApp.

### Key Highlights
- **Two-Tab Navigation:** Switch cleanly between **About Me** and **What I Do & Websites I Build** without cluttering the page.
- **Warm Editorial Palette:** Warm cream (`#f6f1e7`) and sand (`#efe8da`) surfaces paired with dark charcoal text (`#23201e`) and terracotta/muted gold accents.
- **3D Scroll Reveal & Hover Interactions:** Cards and photography animate forward into view as you scroll (`IntersectionObserver`) and respond smoothly on hover.
- **Direct WhatsApp Contact:** Pre-filled inquiry links wired into the top bar, hero section, footer strip, and mobile floating button.
- **Mobile & Desktop Scaling:** Layout grids and mobile font sizes are tuned so phones stay readable without oversized headings.

---

## Folder Structure

```text
My_Website/
├── app.py                # Flask route, profile data dictionary, and WhatsApp URL builder
├── templates/
│   └── index.html        # Page markup, Jinja2 loops, tab switching, and 3D reveal script
├── static/
│   └── style.css         # Theme variables, layout grids, 3D transforms, and responsive rules
└── README.md             # Project documentation
