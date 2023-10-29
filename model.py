from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS


# Define a function to answer medical questions using the GPT-2 model
def answer_medical_question(question):
    # Load the GPT-2 model for text generation
    generator = pipeline("text-generation", model="gpt2")
    # pl = pipeline(
    #     "text-generation",
    #     model="medalpaca/medalpaca-13b",
    #     tokenizer="medalpaca/medalpaca-13b",
    # )

    # Generate an answer based on the input question
    answer = generator(question, max_length=100, num_return_sequences=1)
    # answer = pl(question, max_length=50, do_sample=True, temperature=0.9)
    # print(answer[0]["generated_text"])
    return answer[0]["generated_text"]


app = Flask(__name__)
CORS(app)


@app.route("/get_answer", methods=["POST"])
def get_answer():
    data = request.get_json()
    print(data)
    question = data["question"]
    # sample_question = input()
    sample_question = question
    # sample_question = "What are the symptoms of diabetes?"

    # Get an answer using the function
    answer = answer_medical_question(sample_question)
    print("Answer:", answer)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
