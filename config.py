import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "farine-dev-secret-change-me")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB max upload

    # Supported languages for the site
    LANGUAGES = ["en", "fr"]
    DEFAULT_LANGUAGE = "fr"  # NUTCHE is francophone-first, English available

    # Contact / consultation booking recipient
    CONTACT_RECEIVER_EMAIL = os.environ.get("CONTACT_RECEIVER_EMAIL", "nutcheproducts@gmail.com")

    # ------------------------------------------------------------------
    # Outgoing mail (used to actually deliver the contact form to
    # CONTACT_RECEIVER_EMAIL). Fill these in the .env file.
    # ------------------------------------------------------------------
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # ------------------------------------------------------------------
    # Database (consultations / contact submissions)
    # ------------------------------------------------------------------
    DATABASE_PATH = os.environ.get("DATABASE_PATH", os.path.join(BASE_DIR, "data", "nutche.db"))

    # ------------------------------------------------------------------
    # Admin panel
    # ------------------------------------------------------------------
    # In production, set ADMIN_USERNAME and ADMIN_PASSWORD (or ADMIN_PASSWORD_HASH)
    # as environment variables instead of relying on these defaults.
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "nutche-admin-2026")
    ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH")  # takes priority if set