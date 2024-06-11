from flask import Flask,render_template,request,jsonify
import random
import string

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")
@app.route("/generate-password",methods=['post'])
def generate_password():
  # getting the posted and assigning the posted data 
    data = request.json
    length = int(data.get("length"))
    include_uppercase = data.get("include_uppercase")
    include_lowercase = data.get("include_lowercase")
    include_numbers = data.get("include_numbers")
    include_special_characters = data.get("include_special_characters")
    include_added_words = data.get("include_added_words")
    include_ambiguous_characters = data.get("include_ambiguous_characters")
    print(include_uppercase,include_lowercase,include_numbers,include_special_characters,include_added_words,include_ambiguous_characters)

#creating the characters to be included the generated password

    uppercase_chars = string.ascii_uppercase
    lowecase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    special_chars = string.punctuation
    ambiguous_chars = "il1Lo0O"

    #combine the selected chars sets
    char_set=''
    if include_uppercase:
        char_set +=uppercase_chars
    if include_lowercase:
        char_set +=lowecase_chars
    if include_numbers:
        char_set +=number_chars
    if include_special_characters:
        char_set +=special_chars
    if include_ambiguous_characters:
        char_set+=ambiguous_chars
    if not include_ambiguous_characters:
        for char in ambiguous_chars:
            char_set = char_set.replace(char,'')
    
    password=''.join(random.choice(char_set) for _ in range(length))
    return jsonify({"password":password})

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)