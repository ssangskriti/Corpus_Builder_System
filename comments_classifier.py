from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

from bangla_comments_separator import bangla_comments

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(bangla_comments)

k = 3
model = KMeans(n_clusters=k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()


def check_similarity(text):
    count1 = count2 = count3 = 0
    for word in text:
        if word in terms[0]:
            count1 += 1
        elif word in terms[1]:
            count2 += 1
        elif word in terms[2]:
            count3 += 1
    if max(count1, count2, count3) == count1:
        return "class1"
    elif max(count1, count2, count3) == count2:
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
# print(classified)

# dumping into a json file
with open("classified_comments.json", 'w') as file:
    json.dump(classified, file)
