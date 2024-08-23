from flask import Flask, render_template, request, jsonify
import string
import secrets

app = Flask(__name__,)

@app.route("/")
# defining the index route and returning what is to be rendered on the page
def index():
    return render_template("index.html")


@app.route("/generate-password", methods=["post"])
# defining the route for the posted data
def generate_password():
    # Using try and except to show and handle any errors during the request
    try:
        # Getting the posted data and assigning it to a variable
        data = request.json
        length = int(data.get("length"))
        include_uppercase = data.get("include_uppercase")
        include_lowercase = data.get("include_lowercase")
        include_numbers = data.get("include_numbers")
        include_special_characters = data.get("include_special_characters")
        include_added_words = data.get("include_added_words")
        include_ambiguous_characters = data.get("include_ambiguous_characters")

        # Defining the characters to be included in the generated password

        uppercase_chars = string.ascii_uppercase
        lowercase_chars = string.ascii_lowercase
        # uppercase_chars = string.ascii_uppercase
        number_chars = string.digits
        special_chars = string.punctuation
        ambiguous_chars = "il1o0O"

        # Checking for characters to be included in the generated password
        # And adding it to an empty string
        char_set = ""
        if include_uppercase:
            char_set += uppercase_chars

        if include_lowercase:
            char_set += lowercase_chars

        if include_numbers:
            char_set += number_chars

        if include_special_characters:
            char_set += special_chars

        if include_ambiguous_characters:
            char_set += ambiguous_chars

        if not include_ambiguous_characters:
            for char in ambiguous_chars:
                char_set = char_set.replace(char, "")

        if include_added_words:
            char_set += "".join(include_added_words)

            # generating the password using char_set and the length specified from the user
        password = "".join(secrets.choice(char_set) for _ in range(length))

        # now we have to calculate the complexity of the password
        if length < 8:
            return jsonify({"password": password, "strength": "Weak"}), 200
        elif length <= 12:
            return jsonify({"password": password, "strength": "Medium"}), 200
        else:
            return jsonify({"password": password, "strength": "Strong"}), 200
        # returning the generated password as the response with a status code of 200
        # return
    except Exception as error:
        # if there's an error maybe during the password generation
        # it returns the error and status code and logs the error for easy  debugging
        app.logger.error(f"Error generating password {error}")
        return jsonify({"error": error}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
