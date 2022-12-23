import os


class Config:

    BOT_TOKEN = os.environ.get("5165073477:AAE_FhVKqYn4AaSUFP7sVYhK9NNbZDNND-E")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("3551539"))

    API_HASH = os.environ.get("a73df1c7f1849be0bb402811f6ffb758")

    CLIENT_ID = os.environ.get("406671440793-2kcmg3jnvafdicb023d0e3vvatq2c0i5.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("1099021840"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
