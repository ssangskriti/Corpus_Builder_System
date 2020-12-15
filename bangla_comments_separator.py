import pandas as pd
import fasttext


# extract comments from csv file
df = pd.read_csv('bkash_comments.csv', sep=';')
df = df[df['message'].notna()]
comments = df["message"]
# print(comments)

# using fasttext pretrained model
PRETRAINED_MODEL_PATH = 'lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

# extracting bangla comments
bangla_comments = []

for comment in comments:
    # comment = ['আমার দেশ বাংলাদেশ']
    predictions = model.predict(comment)
    # print(predictions[0])
    if predictions[0][0]== '__label__bn':
        bangla_comments.append(comment)

# for bnc in bangla_comments:
#     print(bangla_comments)


