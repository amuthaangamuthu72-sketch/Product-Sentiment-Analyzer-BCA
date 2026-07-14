from flask import *
from flask_cors import CORS
from db import get_connection
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products", methods=["POST"])
def add_product():
    try:
        data = request.get_json()

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO products (product_name, review, polarity, sentiment)
            VALUES (:1, :2, :3, :4)
        """, (
            data["product_name"],
            data["review"],
            data["polarity"],
            data["sentiment"]
        ))
        print("Received:",data)
        cursor.execute("SELECT USER FROM DUAL")
        print(cursor.fetchone())
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Data Inserted Successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/search", methods=["GET"])
def search():
    product = request.args.get("product")

    return jsonify([
        {
            "review": f"{product} is amazing",
            "sentiment": "Positive"
        },
        {
            "review": f"{product} is average",
            "sentiment": "Neutral"
        },
        {
            "review": f"{product} is bad",
            "sentiment": "Negative"
        }
    ])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)