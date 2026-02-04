from flask import Flask, render_template, request, redirect, url_for, session
import pyotp
import qrcode
import io
import base64

app = Flask(__name__)
app.secret_key = "super-secret-key"


# -------------------------
# Password strength check
# -------------------------
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*()-_+=<>?/{}[]|" for c in password):
        return False
    return True


# -------------------------
# Routes
# -------------------------
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not is_strong_password(password):
        return render_template(
            "login.html",
            error="Password must contain uppercase, lowercase, number & symbol"
        )

    session.clear()
    session["email"] = email
    session["totp_secret"] = pyotp.random_base32()

    return redirect(url_for("otp_page"))


@app.route("/otp")
def otp_page():
    if "email" not in session:
        return redirect(url_for("login_page"))

    if session.get("verified"):
        return redirect(url_for("dashboard"))

    secret = session["totp_secret"]
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(
        name=session["email"],
        issuer_name="2FA Demo App"
    )

    img = qrcode.make(uri)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_code = base64.b64encode(buffer.getvalue()).decode()

    return render_template("otp.html", qr_code=qr_code)


@app.route("/verify-otp", methods=["POST"])
def verify_otp():
    if "totp_secret" not in session:
        return redirect(url_for("login_page"))

    user_otp = request.form.get("otp")
    totp = pyotp.TOTP(session["totp_secret"])

    if totp.verify(user_otp):
        session["verified"] = True
        return redirect(url_for("dashboard"))
    else:
        return render_template("otp.html", error="Invalid OTP")


@app.route("/dashboard")
def dashboard():
    if not session.get("verified"):
        return redirect(url_for("login_page"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=True)
