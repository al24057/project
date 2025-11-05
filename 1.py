import MeCab

t=MeCab.Tagger()

def extract_data(text):
    data={"nouns":[], "verbs":[], "adj":[], "adjv":[], "adv":[], "auxv":[], "con":[]}
    result=t.parseToNode(text)
    while result:
        features=result.feature.split(",")
        node=features[0]
        if len(features)>7:
            base_form=features[7]
        else:
            base_form=result.surface
        
        if node=="名詞":
            data["nouns"].append(base_form)
        elif node=="動詞":
            data["verbs"].append(base_form)
        elif node=="形容詞":
            data["adj"].append(base_form)
        elif node=="形状詞":
            data["adjv"].append(base_form)
        elif node=="副詞":
            data["adv"].append(base_form)
        elif node=="助動詞":
            data["auxv"].append(base_form)
        elif node=="連体詞":
            data["con"].append(base_form)
        result=result.next
        
    print(data)
    
    return data

sentence=input("検索->")
data=extract_data(sentence)

dataset=[
    {"sentence":"全世界にばらまかれたコンピュータウイルスについて"},
    {"sentence":"常時配信している最近噂のあのユーチューバーに迫る！"},
    {"sentence":"大学2年生の秋葉さんが書道で理事長賞を受賞！"},
    {"sentence":"世界で限りある資源の減少の様子を今後も観察するだけでいいのか？"},
    {"sentence":"世界の至る所で常時踊ってしまうという奇行が大流行しており、動画サイトでもその様子が配信されている問題について"},
]



for i in range(len(dataset)):
    dataset[i]["nouns"]=extract_data(dataset[i]["sentence"])["nouns"]
    dataset[i]["verbs"]=extract_data(dataset[i]["sentence"])["verbs"]
    dataset[i]["adj"]=extract_data(dataset[i]["sentence"])["adj"]
    dataset[i]["adjv"]=extract_data(dataset[i]["sentence"])["adjv"]
    dataset[i]["adv"]=extract_data(dataset[i]["sentence"])["adv"]
    dataset[i]["auxv"]=extract_data(dataset[i]["sentence"])["auxv"]
    dataset[i]["con"]=extract_data(dataset[i]["sentence"])["con"]

score=[]

for j in range(len(dataset)):
    a=0
    for i in range(len(data["nouns"])):
        if data["nouns"][i] in dataset[j]["nouns"]:
            a=a+2
    for i in range(len(data["verbs"])):
        if data["verbs"][i] in dataset[j]["verbs"]:
            a=a+1
    for i in range(len(data["adj"])):
        if data["adj"][i] in dataset[j]["adj"]:
            a=a+1
    for i in range(len(data["adjv"])):
        if data["adjv"][i] in dataset[j]["adjv"]:
            a=a+0.5
    for i in range(len(data["adv"])):
        if data["adv"][i] in dataset[j]["adv"]:
            a=a+0.3
    
        
    score.append(a)
    
for i in range(len(dataset)):
    dataset[i]["score"]=score[i]

for i in range(len(dataset)-1):
    for j in range(len(dataset)-i-1):
        if(dataset[j]["score"]<dataset[j+1]["score"]):
            temp=dataset[j]
            dataset[j]=dataset[j+1]
            dataset[j+1]=temp
            
for i in range(len(dataset)):
    print(dataset[i]["sentence"])

