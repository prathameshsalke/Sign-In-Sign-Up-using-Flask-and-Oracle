from flask import Flask, render_template, request, jsonify
import oracledb
import hashlib

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    try:
        con = oracledb.connect(
            user="system",
            password="Tejas@123",   # change if needed
            dsn="localhost/XEPDB1"
        )
        print("✅ Database connected successfully")
        return con
    except Exception as e:
        print("❌ Database connection failed")
        print(e)
        raise

# ---------------- PASSWORD HASH ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- LOAD PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- SIGN UP ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    full_name = data.get("username")

    hashed_password = hash_password(password)

    try:
        con = get_connection()
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM users WHERE email = :1", [email])
        if cur.fetchone()[0] > 0:
            return jsonify({"error": "Email already registered"}), 409

        cur.execute("""
            INSERT INTO users (email, password, full_name)
            VALUES (:1, :2, :3)
        """, [email, hashed_password, full_name])

        con.commit()
        cur.close()
        con.close()

        return jsonify({"message": "Signup successful"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    hashed_password = hash_password(password)

    try:
        con = get_connection()
        cur = con.cursor()

        cur.execute("SELECT password FROM users WHERE email = :1", [email])
        row = cur.fetchone()

        cur.close()
        con.close()

        if row is None:
            return jsonify({"error": "User not found"}), 404
        if row[0] != hashed_password:
            return jsonify({"error": "Invalid password"}), 401

        return jsonify({"message": "Login successful"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------- RUN ----------------
if __name__ == "__main__":
    print("🚀 Flask server starting...")
    app.run(debug=True)
