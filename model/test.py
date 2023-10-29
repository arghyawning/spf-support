from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA

from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS


DB_FAISS_PATH = "vectorstore/db_faiss"

custom_prompt_template = """To respond to the user's inquiry, use the following details.
Instead of attempting to come up with an answer, just acknowledge that you don't know. Do not try to make up an answer.
Context: {context}
Question: {question}

Please respond only with helpful responses. 
Here's a helpful answer.
"""


# Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
    )
    return llm


# QA Model Function
def qa_bot():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = PromptTemplate(
        template=custom_prompt_template, input_variables=["context", "question"]
    )
    print(qa_prompt)
    # qa = retrieval_qa_chain(llm, qa_prompt, db)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": qa_prompt},
    )

    return qa


# output function
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({"query": query})
    print("--------------------------------------------------")
    print(response["result"])
    return response["result"]


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
    # answer = answer_medical_question(sample_question)
    answer = final_result(sample_question)
    print("Answer:", answer)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
