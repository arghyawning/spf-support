import pandas as pd
paragraphs_data = data["data"][0]["paragraphs"]

# Create a list to store the data for each paragraph
paragraph_data_list = []

for paragraph in paragraphs_data:
    # Extract the relevant data for each paragraph
    paragraph_qas = paragraph["qas"]
    for qa in paragraph_qas:
        qa_data = {
            # "url": qa["url"],
            "id": qa["id"],
            "question": qa["question"],
            # "is_impossible": qa["is_impossible"]
        }
        if "answers" in qa:
            qa_data["answers"] = qa["answers"][0]["text"]
        else:
            qa_data["answers"] = None
        paragraph_data_list.append(qa_data)

# Create a Pandas DataFrame from the list of paragraph data
df = pd.DataFrame(paragraph_data_list)

# Display the DataFrame
# print(df)
df
