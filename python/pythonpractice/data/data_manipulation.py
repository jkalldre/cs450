from pandas import *
from numpy  import *
import arr             # Clean code and put bulky arrays in other file
from sklearn.preprocessing import normalize

def main():
    set_printoptions(suppress=True, threshold=inf) #np
    data = read_csv('./adult_data.csv', header = 0, na_values=' ?')
    col_names = ["Age", "Workclass" , "Fnlwgt"        , "Education",
                    "Education-num" , "Marital-status", "Occupation",
                    "Relationship"  , "Race"          , "Sex",
                    "Capital-gain"  , "Capital-loss"  , "Hours-per-week",
                    "Native-country", "50k_threshold"]

    cat_col = ["Workclass", "Education", "Marital-status", "Occupation",
        "Relationship", "Race", "Sex"   , "Native-country"
        , "50k_threshold"]

    data.columns = col_names


    cols = [arr.workclass, arr.education, arr.marital_status, arr.occupation
            , arr.relationship, arr.race, arr.sex, arr.native_country
            , arr.threshold]

# Replace all categories
    for j in range(len(cols)):
        for i in range(len(cols[j])):
            data[cat_col[j]] = data[cat_col[j]].replace(cols[j][i], int(i))

# Convert to numPy ARRAY
    npdata = data.as_matrix(columns=None)
    av = getAv(npdata)

# Replace NaN with average of col
    for row in npdata:
        for col_i in range(len(row)):
            if isnan(row[col_i]):
                row[col_i] = av[col_i]

    # print(npdata[-19])
    npdata_normal = normalize(npdata, axis=1,return_norm=True)

    print len(npdata), len(npdata[0])
    for item in npdata:
        print item

def getAv(values):
    s = [nansum(x) for x in zip(*values)]
    av = [x/(len(values)) for x in s]
    # print av
    return av

main()
