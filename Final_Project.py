import json

# Read Files

with open('config.json') as f:
    conf = json.load(f)

c1 = len(open(conf['cluster-files'][0]).readlines())
file1 = conf['cluster-files'][0]
with open(file1) as fp1:
    file1 = fp1.readlines()
file1_lines = ['']*c1
for i in range(0,c1,1):
    file1_lines[i]=file1[i]

c2 = len(open(conf['cluster-files'][1]).readlines())
file2 = conf['cluster-files'][1]
with open(file2) as fp2:
    file2 = fp2.readlines()
file2_lines = ['']*c2
for i in range(0,c2,1):
    file2_lines[i]=file2[i]

c3 = len(open(conf['deps-files'][0]).readlines())
file3 = conf['deps-files'][0]
with open(file3) as fp3:
    file3 = fp3.readlines()
file3_lines = [''] * c3
w, h = 3, c3
file3_space = [[0 for x in range(w)] for y in range(h)]
for l in range(0, c3, 1):
    file3_lines[l] = file3[l].strip("\n")
    file3_space[l] = file3_lines[l].split(" ")

c4 = len(open(conf['deps-files'][1]).readlines())
file4 = conf['deps-files'][1]
with open(file4) as fp4:
    file4 = fp4.readlines()
file4_lines = [''] * c4
w, h = 3, c4
file4_space = [[0 for x1 in range(w)] for y1 in range(h)]
for l1 in range(0, c4, 1):
    file4_lines[l1] = file4[l1].strip("\n")
    file4_space[l1] = file4_lines[l1].split(" ")


# Comparison Tool
if c1>c2:
    xx=c1
else:
    xx=c2
removals=['']*xx
r=0
additions=['']*xx
a=0
no_change=['']*xx
n=0
for k in range(0,c2,1):
    if file2_lines[k] not in file1_lines:
        additions[a]=file2_lines[k].strip("\r\n")
        a=a+1
    else:
        no_change[n] = file2_lines[k].strip("\r\n")
        n = n + 1
for i in range(0,c1,1):
    if file1_lines[i] not in file2_lines:
        removals[r] = file1_lines[i].strip("\r\n")
        r=r+1

# graphics
g_a=[]
for add in range(0, a, 1):
    if " graphics " in additions[add]:
        g_a.append(additions[add].replace("contain graphics ",""))
g_r = []
for remove in range(0, r, 1):
    if " graphics " in removals[remove]:
        g_r.append(removals[remove].replace("contain graphics ",""))
g_u = []
for same in range(0, n, 1):
    if " graphics " in no_change[same]:
        g_u.append(no_change[same].replace("contain graphics ",""))
# io
i_a = []
for add in range(0, a, 1):
    if " io " in additions[add]:
        i_a.append(additions[add].replace("contain io ",""))
i_r = []
for remove in range(0, r, 1):
    if " io " in removals[remove]:
        i_r.append(removals[remove].replace("contain io ",""))
i_u = []
for same in range(0, n, 1):
    if " io " in no_change[same]:
        i_u.append(no_change[same].replace("contain io ",""))
# sql
s_a = []
for add in range(0, a, 1):
    if " sql " in additions[add]:
        s_a.append(additions[add].replace("contain sql ",""))
s_r = []
for remove in range(0, r, 1):
    if " sql " in removals[remove]:
        s_r.append(removals[remove].replace("contain sql ",""))
s_u = []
for same in range(0, n, 1):
    if " sql " in no_change[same]:
        s_u.append(no_change[same].replace("contain sql ",""))
# networking
n_a = []
for add in range(0, a, 1):
    if " networking " in additions[add]:
        n_a.append(additions[add].replace("contain networking ",""))
n_r = []
for remove in range(0, r, 1):
    if " networking " in removals[remove]:
        n_r.append(removals[remove].replace("contain networking ",""))
n_u = []
for same in range(0, n, 1):
    if " networking " in no_change[same]:
        n_u.append(no_change[same].replace("contain networking ",""))
# no_match
no_a = []
for add in range(0, a, 1):
    if " no_match " in additions[add]:
        no_a.append(additions[add].replace("contain no_match ",""))
no_r = []
for remove in range(0, r, 1):
    if " no_match " in removals[remove]:
        no_r.append(removals[remove].replace("contain no_match ",""))
no_u = []
for same in range(0, n, 1):
    if " no_match " in no_change[same]:
        no_u.append(no_change[same].replace("contain no_match ",""))

data={
    "graphics":{
        "added": g_a,
        "removed": g_r,
        "unchanged":g_u
    },
    "io":{
        "added": i_a,
        "removed": i_r,
        "unchanged": i_u
    },
    "sql":{
        "added": s_a,
        "removed": s_r,
        "unchanged": s_u
    },
    "networking":{
        "added": n_a,
        "removed": n_r,
        "unchanged": n_u
    },
    "no_match":{
        "added": no_a,
        "removed": no_r,
        "unchanged": no_u
    }
}

# JSON for Comparison Tool
with open('compare.json', 'w') as outfile:
    json.dump(data, outfile)


# Bar Graph

# Version 1
key_list = [''] * c3
ctr = [0] * c3
length_of_value=0
top_ten = [0]*5
bar_list={}
split_key=['']*2
split_val=['']*2
for z in range(0, c3, 1):
    if "$" in file3_space[z][1]:
        split_key=file3_space[z][1].split("$")
    else:
        split_key[0]=file3_space[z][1]
    key = split_key[0]
    value = [''] * c3
    if key not in key_list:
        if "$" in file3_space[z][2]:
            split_val=file3_space[z][2].split("$")
        else:
            split_val[0]=file3_space[z][2]
        value.append(split_val[0])
        value = filter(None, value)
        ctr[z] = 1
        key_list.append(key)
        for y in range(z + 1, c3, 1):
            if "$" in file3_space[y][1]:
                split_key = file3_space[y][1].split("$")
            else:
                split_key[0] = file3_space[y][1]
            if key == split_key[0]:
                if "$" in file3_space[y][2]:
                    split_val = file3_space[y][2].split("$")
                else:
                    split_val[0] = file3_space[y][2]
                value.append(split_val[0])
                ctr[z] = ctr[z] + 1
                value = filter(None, value)
        if length_of_value<len(value):
            length_of_value = len(value)
            top_ten.append(length_of_value)
            top_ten.sort(reverse=True)
            top_ten = filter(None, top_ten)
            if length_of_value in top_ten:
                bar_list[key]=value

# Version 2
key_list2 = bar_list.keys()
bar_list2 = {}
done_key2=['']*5
for z in range(0, c4, 1):
    if "$" in file4_space[z][1]:
        split_key=file4_space[z][1].split("$")
    else:
        split_key[0]=file4_space[z][1]
    key2 = split_key[0]
    value2 = [''] * c4
    if key2 in key_list2 and key2 not in done_key2:
        done_key2.append(key2)
        if "$" in file4_space[z][2]:
            split_val = file4_space[z][2].split("$")
        else:
            split_val[0] = file4_space[z][2]
        value2.append(split_val[0])
        value2 = filter(None, value2)
        for y in range(z + 1, c4, 1):
            if "$" in file4_space[y][1]:
                split_key = file4_space[y][1].split("$")
            else:
                split_key[0] = file4_space[y][1]
            if key2 == split_key[0]:
                if "$" in file4_space[y][2]:
                    split_val = file4_space[y][2].split("$")
                else:
                    split_val[0] = file4_space[y][2]
                value2.append(split_val[0])
                value2 = filter(None, value2)
        bar_list2[key2]=value2
        length_of_value2=len(value2)

# JSON for Bar Graph
bar_dict={}
bar_dict[conf['deps-files'][0].split("_")[0]]=bar_list
bar_dict[conf['deps-files'][1].split("_")[0]]=bar_list2
with open('bar_graph.json', 'w') as outfile:
    outfile.write(json.dumps(bar_dict,sort_keys=True))


# Matrix Representation

d={}
all_cluster = []
for k in range(0, c1, 1):
    cluster = file1_lines[k].strip("\r\n").split(" ")[1]
    file = file1_lines[k].strip("\r\n").split(" ")[2]
    a = []
    all_cluster.append(file)
    if cluster in d:
        a = d.get(cluster)
    a.append(file)
    d[cluster] = a
outerC = 0
mainOutput1 = {}
mainOutput2 = {}
finalOutput = {}
finalOutput["v1#"+conf['deps-files'][0].split("_")[0]] = {}
finalOutput["v2#"+conf['deps-files'][1].split("_")[0]] = {}
for k in range(0, c3, 1):
    deps1 = file3_lines[k].strip("\r\n").split(" ")[1]
    deps2 = file3_lines[k].strip("\r\n").split(" ")[2]
    arr = deps1.split("$")
    name = arr[0]
    arr2 = deps2.split("$")
    name2 = arr2[0]
    count = 0
    jsonVal = {}
    if name != name2:
        for key in d:
            if name in d[key] or name2 in d[key]:
                outer = {}
                if name in d[key]:
                    outer[key] = name
                    jsonVal["first"] = outer
                if name2 in d[key]:
                    outer[key] = name2
                    jsonVal["second"] = outer
                count = count+1
        if count == 2:
            outerC= outerC+1
            innerJ = {}
            key = jsonVal["first"].keys()[0]
            arr = []
            arr.append(name2)
            if mainOutput1.has_key(key):
                if mainOutput1[key].has_key(jsonVal["second"].keys()[0]):
                    val = mainOutput1[key][jsonVal["second"].keys()[0]]
                    if val.has_key(name):
                        values = val[name]
                        if name2 not in values:
                            values.append(name2)
                        mainOutput1[key][jsonVal["second"].keys()[0]][name] = values
                    else:
                        mainOutput1[key][jsonVal["second"].keys()[0]][name] = arr
                else:
                    mainOutput1[key][jsonVal["second"].keys()[0]] = {}
                    mainOutput1[key][jsonVal["second"].keys()[0]][name] = arr

            else:
                mainOutput1[key] = {}
                mainOutput1[key][jsonVal["second"].keys()[0]] = {}
                mainOutput1[key][jsonVal["second"].keys()[0]][name] = arr



for k in range(0, c4, 1):
    deps1 = file4_lines[k].strip("\r\n").split(" ")[1]
    deps2 = file4_lines[k].strip("\r\n").split(" ")[2]
    arr = deps1.split("$")
    name = arr[0]
    arr2 = deps2.split("$")
    name2 = arr2[0]
    count = 0
    jsonVal = {}
    if name != name2:
        for key in d:
            if name in d[key] or name2 in d[key]:
                outer = {}
                if name in d[key]:
                    outer[key] = name
                    jsonVal["first"] = outer
                if name2 in d[key]:
                    outer[key] = name2
                    jsonVal["second"] = outer
                count +=1
        if count == 2:
            outerC+=1
            innerJ = {}
            key = jsonVal["first"].keys()[0]
            arr = []
            arr.append(name2)
            if mainOutput2.has_key(key):
                if mainOutput2[key].has_key(jsonVal["second"].keys()[0]):
                    val = mainOutput2[key][jsonVal["second"].keys()[0]]
                    if val.has_key(name):
                        values = val[name]
                        if name2 not in values:
                            values.append(name2)
                        mainOutput2[key][jsonVal["second"].keys()[0]][name] = values
                    else:
                        mainOutput2[key][jsonVal["second"].keys()[0]][name] = arr
                else:
                    mainOutput2[key][jsonVal["second"].keys()[0]] = {}
                    mainOutput2[key][jsonVal["second"].keys()[0]][name] = arr

            else:
                mainOutput2[key] = {}
                mainOutput2[key][jsonVal["second"].keys()[0]] = {}
                mainOutput2[key][jsonVal["second"].keys()[0]][name] = arr


finalOutput["v1#"+conf['deps-files'][0].split("_")[0]] = mainOutput1;
finalOutput["v2#"+conf['deps-files'][1].split("_")[0]] = mainOutput2;



# JSON for Matrix Representation
with open('matrix.json', 'w') as outfile:
    outfile.write(json.dumps(finalOutput,sort_keys=True))



# Most Important Files

# Version 1
key_list11 = [''] * c3
ctr11 = [0] * c3
length_of_value11=0
top_ten11 = [0]*5
bar_list11={}
split_key11=['']*2
split_val11=['']*2


for z in range(0, c3, 1):
    if "$" in file3_space[z][2]:
        split_key11=file3_space[z][2].split("$")
    else:
        split_key11[0]=file3_space[z][2]
    key11 = split_key11[0]
    value11 = [''] * c3
    if key11 not in key_list11 and key11 in all_cluster:
        if "$" in file3_space[z][1]:
            split_val11=file3_space[z][1].split("$")
        else:
            split_val11[0]=file3_space[z][1]
        if split_val11[0] in all_cluster:
            value11.append(file3_space[z][1])
        value11 = filter(None, value11)
        ctr11[z] = 1
        key_list11.append(key11)
        for y in range(z + 1, c3, 1):
            if "$" in file3_space[y][2]:
                split_key11 = file3_space[y][2].split("$")
            else:
                split_key11[0] = file3_space[y][2]
            if key11 == split_key11[0]:
                if "$" in file3_space[y][1]:
                    split_val11 = file3_space[y][1].split("$")
                else:
                    split_val11[0] = file3_space[y][1]
                if split_val11[0] in all_cluster:
                    value11.append(file3_space[y][1])
                    ctr11[z] = ctr11[z] + 1
                    value11 = filter(None, value11)
        if length_of_value11<len(value11):
            length_of_value11 = len(value11)
            top_ten11.append(length_of_value11)
            top_ten11.sort(reverse=True)
            top_ten11 = filter(None, top_ten11)
            if length_of_value11 in top_ten11:
                bar_list11[key11]=value11

# Version 2
key_list21 = bar_list11.keys()
bar_list21 = {}
done_key21=['']*5
for z in range(0, c4, 1):
    if "$" in file4_space[z][2]:
        split_key11=file4_space[z][2].split("$")
    else:
        split_key11[0]=file4_space[z][2]
    key21 = split_key11[0]
    value21 = [''] * c4
    if key21 in key_list21 and key21 not in done_key21:
        done_key21.append(key21)
        if "$" in file4_space[z][1]:
            split_val11 = file4_space[z][1].split("$")
        else:
            split_val11[0] = file4_space[z][1]
        if split_val11[0] in all_cluster:
            value21.append(file4_space[z][1])
        value21 = filter(None, value21)
        for y in range(z + 1, c4, 1):
            if "$" in file4_space[y][2]:
                split_key11 = file4_space[y][2].split("$")
            else:
                split_key11[0] = file4_space[y][2]
            if key21 == split_key11[0]:
                if "$" in file4_space[y][1]:
                    split_val11 = file4_space[y][1].split("$")
                else:
                    split_val11[0] = file4_space[y][1]
                if split_val11[0] in all_cluster:
                    value21.append(file4_space[y][1])
                value21 = filter(None, value21)
        bar_list21[key21]=value21
        length_of_value21=len(value21)

# JSON for Bar Graph 2
bar_dict2={}
bar_dict2[conf['deps-files'][0].split("_")[0]]=bar_list11
bar_dict2[conf['deps-files'][1].split("_")[0]]=bar_list21
with open('most_important_class.json', 'w') as outfile2:
    outfile2.write(json.dumps(bar_dict2,sort_keys=True))
