dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
 'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
 'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193, 
 'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}
dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)

import queue as Q
start='Arad'
goal='Bucharest'
result=''

def BFS(city,cityq,visitdq):
    global result
    if city==start:
        result=result+'\n'+city
    for eachcity in dict_gn[city].keys():
        if eachcity==goal:
            result=result+'\n'+eachcity
            return
        if eachcity not in cityq.queue and eachcity not in visitdq.queue:
            cityq.put(eachcity)
            result=result+'\n'+eachcity
    visitdq.put(city)
    BFS(cityq.get(),cityq,visitdq)

def main():
    cityq=Q.Queue()
    visitdq=Q.Queue()
    BFS(start,cityq,visitdq)
    print("BFS Traversal from ",start," to ",goal," is: ")
    print(result)
main()