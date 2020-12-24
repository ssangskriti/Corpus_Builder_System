from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

from bangla_comments_separator import bangla_comments

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(bangla_comments)

k = 3
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

def check_similarity(text):
    y = vectorizer.transform([text])
    prediction = model.predict(y)

    if prediction == [0]:
        return "class1"
    elif prediction == [1]:
        return "class2"
    else:
        return "class3"


classified = {
    "class1": [],
    "class2": [],
    "class3": []
}

for line in bangla_comments:
    class_name = check_similarity(line)
    classified[class_name].append(line)

with open("classified_comments.json", 'w') as file:
    json.dump(classified, file)
