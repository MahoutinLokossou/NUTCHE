import smtplib
from email.message import EmailMessage

from flask import Flask, render_template, request, redirect, url_for, session, flash

from config import Config
from translations import translate

app = Flask(__name__)
app.config.from_object(Config)


def send_contact_email(name, sender_email, phone, subject, message_body):
    """Send the contact form submission to CONTACT_RECEIVER_EMAIL.

    Requires MAIL_USERNAME / MAIL_PASSWORD to be set (see .env).
    Raises on failure so the caller can show an error to the visitor.
    """
    mail_username = app.config["MAIL_USERNAME"]
    mail_password = app.config["MAIL_PASSWORD"]

    if not mail_username or not mail_password:
        raise RuntimeError(
            "MAIL_USERNAME / MAIL_PASSWORD are not configured in .env"
        )

    email_msg = EmailMessage()
    email_msg["Subject"] = f"New contact form message from {name}"
    email_msg["From"] = mail_username
    email_msg["To"] = app.config["CONTACT_RECEIVER_EMAIL"]
    # So hitting "Reply" in the inbox replies straight to the visitor
    email_msg["Reply-To"] = sender_email

    body_lines = [
        f"Name: {name}",
        f"Email: {sender_email}",
        f"Phone: {phone or '-'}",
        f"Subject: {subject or '-'}",
        "",
        "Message:",
        message_body,
    ]
    email_msg.set_content("\n".join(body_lines))

    with smtplib.SMTP(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]) as server:
        server.starttls()
        server.login(mail_username, mail_password)
        server.send_message(email_msg)


# ---------------------------------------------------------------------------
# Language handling
# ---------------------------------------------------------------------------

def get_current_language() -> str:
    """Return the active language for this session, defaulting per config."""
    return session.get("lang", app.config["DEFAULT_LANGUAGE"])


@app.context_processor
def inject_translation_helper():
    """Makes t('some.key') and current_lang available in every template."""
    lang = get_current_language()

    def t(key: str) -> str:
        return translate(key, lang)

    return {"t": t, "current_lang": lang, "languages": app.config["LANGUAGES"]}


@app.route("/set-language/<lang_code>")
def set_language(lang_code):
    if lang_code in app.config["LANGUAGES"]:
        session["lang"] = lang_code
    # Send the visitor back to the page they were on
    return redirect(request.referrer or url_for("home"))


# ---------------------------------------------------------------------------
# Page routes
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("contact.form.error", "error")
        else:
            try:
                send_contact_email(name, email, phone, subject, message)
                flash("contact.form.success", "success")
            except Exception:
                app.logger.exception("Failed to send contact form email")
                flash("contact.form.send_error", "error")

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
