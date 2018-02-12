from collections import Counter
from math        import log
from my_dtclassifier import Node
from my_dtclassifier import Tree
from my_dtclassifier import DTModel

dataset = [
     ['good','high','good','yes']    #0
    ,['good','high','poor','yes']    #1
    ,['good','low' ,'good','yes']    #2
    ,['good','low' ,'poor','no' ]    #3
    ,['average','high','good','yes'] #4
    ,['average','low' ,'poor','no' ] #5
    ,['average','high','poor','yes'] #6
    ,['average','low','good','no']   #7
    ,['low','high','good','yes']     #8
    ,['low','high','poor','no' ]     #9
    ,['low','low' ,'good','no']      #10
    ,['low','low' ,'poor','no']]     #11


def transpose(dataset):
    t_dataset = []
    for i in range(len(dataset[0])):
        newlist   = []
        for j in range(len(dataset)):
            newlist.append(dataset[j][i])
        t_dataset.append(newlist)
    return t_dataset

def assign_pair(data,target):
    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col] = [data[row][col],target[col]]
    return data

def get_cate(list):
    count = Counter(list)
    return count.keys()

def eval_by_cat(categories,paired):
    branches = {}
    for i in range(len(categories)):
        branches[categories[i]] = []
    for each in paired:
        branches[each[0]].append(each[1])
    for each in categories:
        branches[each] = [get_av_branch(branches[each])
                          ,arr_to_ratio(branches[each])]
    return cat_av(branches,len(paired)), branches

def cat_av(branches,num_entries):
    summ = 0
    for each in branches.values():
        over = sum(each[1])
        summ += (each[0] * (over/float(num_entries)))
    return summ

def arr_to_ratio(arr):
    count = Counter(arr)
    newarr = []
    # if len(count.keys()) == 1:
        # return count.keys()[0]
    # else:
    for each in count.iteritems():
        newarr.append(each[1])
    return newarr

def get_av_branch(arr):
    ratio = arr_to_ratio(arr)
    # print ratio
    summ = sum(ratio)
    entp = 0
    for s in ratio:
        p = (s/float(summ))
        entp += -(p)*log(p,2)
    return entp

def exclude_eval_by_cat(categories,paired, exclude):
    results = []
    for i in range(len(categories)):
        if i != exclude:
            entp, branches = eval_by_cat(categories[i],paired[i])
            results.append([i
                           ,entp
                           ,branches])
    return results

def most_gain(arr):
    sml = [-1,10000]
    for each in arr:
        if each[1] < sml[1]:
            sml = each
    return [sml[0], sml[2]]

def main():
    t_dataset = transpose(dataset)
    data = t_dataset[0:-1]
    target = t_dataset[-1]
    categories = []
    for each in data:
        categories.append(get_cate(each))

    paired = assign_pair(data,target)

    init_eval = exclude_eval_by_cat(categories,paired,len(categories))
    most = most_gain(init_eval)
    root = Node(most[0],most[1])
    # print "Name:",root.name, "Branches:",root.branches
    branches = {}
    for each in root.branches.keys():
        branches[each] = []

    working_parent = root

    for i in range(len(paired[working_parent.name])):
        branches[paired[working_parent.name][i][0]].append(i)
    # print branches

    # Begin Recursion
    for key in branches.keys():
        recurse(branches[key],working_parent,categories,paired)
        # print patch_arr(branches[key],paired)

    root.display_children()
    # next_most = most_gain(exclude_eval_by_cat(categories,paired,most[0]))
    # next_node = Node(next_most[0],next_most[1])
    # print "Name:",next_node.name, "Branches:",next_node.branches

def patch_arr(indexes, arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append([])
        for j in indexes:
            newarr[i].append(arr[i][j])
    return newarr

def always(arr):
    for i in range(len(arr)-1):
        if arr[i][1] != arr[i+1][1]:
            return False
    return True

def recurse(indexes,root,categories,paired):
    relative_paired = patch_arr(indexes,paired)
    if always(relative_paired[0]):
        leaf = Node(relative_paired[0][0][1])
        leaf.give_parent(root)
        root.give_child(leaf)
        # print leaf.name
    else:
        next_info = most_gain(exclude_eval_by_cat(categories,relative_paired,root.name))
        next_node = Node(next_info[0],next_info[1])
        next_node.give_parent(root)
        root.give_child(next_node)
        branches = {}
        for each in next_node.branches.keys():
            branches[each] = []
        for i in range(len(relative_paired[next_node.name])):
            branches[relative_paired[next_node.name][i][0]].append(i)
        # print branches
        # Repeat Recursion
        for key in branches.keys():
            recurse(branches[key],next_node,categories,relative_paired)


main()
