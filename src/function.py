import pickle
from pathlib import Path

def pass_data(repo_data):
    func_dict = {0: 'Data Analysis', 1:'Data Visualization', 2:'Data Preparation'}
    excerpts = repo_data['description']
    input_excerpt= ""
    for excerpt in excerpts:
        input_excerpt += excerpt['excerpt']
    print(input_excerpt)
    #print(excerpt,type(repo_data))
    path = Path(__file__).parent.absolute()
    default_funcion =  str(path)+"/models/function.sk"
    classifier = pickle.load(open(default_funcion, 'rb'))
    predict = classifier.predict([input_excerpt])
    repo_data['function'] = func_dict[predict[0]]
    return repo_data