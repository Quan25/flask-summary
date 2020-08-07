import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import json


def Grader():
    with open("Student.json") as student:
        studentData=json.load(student)

    with open("Instructor.json") as instuctor:
        instructorData=json.load(instuctor)

    # Term-Document Matrix (TDM) for ‘Instructor’ class
    Instructor_docs = [instructorData['Instructor']]
    Student_docs = studentData['Student']
    #Student_docs = student
    vec_Instructor = CountVectorizer()
    X_Instructor = vec_Instructor.fit_transform(Instructor_docs)
    tdm_Instructor = pd.DataFrame(X_Instructor.toarray(), columns=vec_Instructor.get_feature_names())

    word_list_Instructor = vec_Instructor.get_feature_names();
    count_list_Instructor = X_Instructor.toarray().sum(axis=0)
    freq_Instructor = dict(zip(word_list_Instructor,count_list_Instructor))

    docs = Instructor_docs + Student_docs

    vec = CountVectorizer()
    X = vec.fit_transform(docs)

    total_features = len(vec.get_feature_names())

    total_cnts_features_Instructor = count_list_Instructor.sum(axis=0)

    total_cnts_features_Instructor


    prob_dict = dict()
    prob_each = []
    cnt=1
    for each in Student_docs:
        for word in word_tokenize(each):

            if word.lower() in freq_Instructor.keys():
                count = freq_Instructor[word.lower()]
            else:
                count = 0

            prob_each.append((count + 1)/(total_cnts_features_Instructor + total_features))
        prob_dict[cnt]=prob_each
        cnt+=1
        prob_each=[]


    prouction = 1
    nb_dict=dict()
    for key, values in prob_dict.items():
        for prob in values:
            prouction = prob * prouction
        nb_dict['Student '+str(key)]=prouction
        prouction=1

    nb_dict={k: v for k, v in sorted(nb_dict.items(), key=lambda item: item[1])}

    cnt = 1
    similarity_dict=dict()
    tfidf = TfidfVectorizer()
    for each in Student_docs:
        document_list = [each] + Instructor_docs
        vecs = tfidf.fit_transform(document_list)
        matrix = ((vecs * vecs.T).A)
        dim = len(Instructor_docs)
        similarity_dict['Student '+ str(cnt)] = matrix[dim:, :dim].mean()
        cnt+=1
    similarity_dict={k: v for k, v in sorted(similarity_dict.items(), key=lambda item: item[1])}


    result = []
    d = {'nb_for_students': list(nb_dict.values())}
    df = pd.DataFrame(data=d)
    mean = df['nb_for_students'].mean()
    for idx, value in enumerate(list(nb_dict.items())):
        result.append((value[1] / mean + similarity_dict[value[0]], value[0],Student_docs[int(value[0][-1:])-1] ))
    result.sort(key = lambda tup : tup[0], reverse = True)
    nb_list=[]
    nb_list=[i[0] for i in result]
    name_list = [i[1] for i in result]

    df = pd.DataFrame(list(zip(name_list, nb_list)),
                   columns =['Name', 'percentile'])

    df['student percentile']=df['percentile'].rank(pct=True)

    percentile = df.to_dict()
    percentile.pop('percentile')
    return (result, Instructor_docs[0], percentile)

def reset():
    open('Student.json', 'w').close()
