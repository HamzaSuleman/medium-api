
import pandas as pd
import random
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from nltk.stem import PorterStemmer
ps = PorterStemmer()

diets = pd.read_csv('diet_properties.csv') 

# fill empty spaces
diets['tags'] = diets['tags'].fillna('')
diets['not_recommand'] = diets['not_recommand'].fillna('')

# convert needed strings to list
def convert(diet_col):
    diet_col2 = diet_col
    for i in range(len(diet_col)):
        diet_col2.loc[i] = ast.literal_eval(diet_col.loc[i]) 
    return diet_col2   

# convert Min Max age to list
def convertMinMaxListAge(main_col,min_col, max_col):
    for i in range(len(min_col)):
        L = []
        for j in range(min_col.loc[i], (max_col.loc[i]+1)):
            L.append(str(j)+"years")
        main_col.loc[i] = L 
    return main_col

# convert Min Max weight to list
def convertMinMaxListWeight(main_col,min_col, max_col):
    for i in range(len(min_col)):
        L = []
        for j in range(min_col.loc[i], (max_col.loc[i]+1)):
            L.append(str(j)+"kg")
        main_col.loc[i] = L 
    return main_col


# applying converting methods
diets['age'] = convertMinMaxListAge(diets['age'], diets['min_age'], diets['max_age'])
diets['weight'] = convertMinMaxListWeight(diets['weight'], diets['min_weight'], diets['max_weight'])
diets['category'] = convert(diets['category'])
diets['gender'] = convert(diets['gender'])
diets['not_recommand'] = convert(diets['not_recommand'])

# removing spaces between the words for recommandation
diets['category'] = diets['category'].apply(lambda x:[i.replace(" ","") for i in x])

# converting list into spaced string
diets['category'] = diets['category'].apply(lambda x:" ".join(x))
diets['gender'] = diets['gender'].apply(lambda x:" ".join(x))
diets['age'] = diets['age'].apply(lambda x:" ".join(x))
diets['weight'] = diets['weight'].apply(lambda x:" ".join(x))

# creating tags for recommandation
diets['tags'] = diets['overview']+" "+diets['category']+" "+diets['gender']+" "+diets['age']+" "+diets['weight']

# create new dataframe
new_diets = diets[['id', 'title','category' ,'gender', 'tags', 'not_recommand']]

# stem means similar words to single term
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_diets['tags'] = new_diets['tags'].apply(stem)

# recommandation function based on category
def get_recommendations(title, cosine_sim, recommand_frame):
    try:
        recommand_list = []
        diet_index = recommand_frame[recommand_frame['category'] == title].index[0]
        distances = cosine_sim[diet_index]
        diets_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[0:5]
        for i in diets_list:
            if (i[1] > 0.6):
                recommand_list.append(recommand_frame.iloc[i[0]].title)
        return recommand_list
                    
    except IndexError:
        recommand_list = []
        for i in range(len(recommand_frame['title'])):
            recommand_list.append(recommand_frame['title'].iloc[i])
        random.shuffle(recommand_list)
        recommand_list = recommand_list[0:4]
        return recommand_list
        
# check disease indexes for removal
def checkDiseaseIndexs(new_diets ,disease1= 'No Selected', disease2 = 'No Selected'):
    remove_index = []
    for i in range(len(new_diets)):
        not_recommand_list = new_diets['not_recommand'].loc[i]
        for j in range(len(not_recommand_list)):
            if(not_recommand_list[j] == disease1 or not_recommand_list[j] == disease2):
                remove_index.append(i)
    remove_index = [*set(remove_index)]
    return remove_index

# remove harmful diets from frame according to person
def removeDietsHarmfulIndexs(remove_index, dataframe):
    deletedframe = dataframe
    deletedframe = dataframe.drop(remove_index)
    deletedframe = deletedframe.reset_index()
    deletedframe = deletedframe.drop('index', axis=1)
    return deletedframe

# tfidf recommandations using diseases
def tfidf_recommand(diet_name, disease1 = 'No Selected' , disease2 = 'No Selected', diets = new_diets):
    remove_index = []
    recommand_frame = diets
    # Remove Harmful Diets based on Given Disease
    if(disease1 != 'No Selected'):
        remove_index = checkDiseaseIndexs(diets, disease1, disease2)
        recommand_frame = removeDietsHarmfulIndexs(remove_index, diets)
    # Let's create vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(recommand_frame['tags'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    # Now let's recommand
    return get_recommendations(diet_name, cosine_sim, recommand_frame)

