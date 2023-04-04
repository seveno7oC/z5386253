list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.remove('bad')
sol.append('including')
sol.insert(2,'good')
sol.extend(list_b)
print(sol)

text = " some text "
text.strip
print(text)

text = " some text "
text.strip()
print(text)

text = " some text "
text.strip('')
print(text)

text = " some text "
text.strip(None)
print(text)

text = " some text "
text.strip('text')
print(text)

w = "What"
i = "IS"
c = "CamelCase?"
a= '{} {} {}'.format(w,i.lower(),c)
print(a)

x = 1
y = 2
y = x
x = y
print(x)


b = 'Problem'
a = f'{a} Parson {b}'
a = f' this is called {b}'
b = print
b(a)


f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")
requiredsuburbs = {"Fairfield",
        "Fairfield East",
        "Fairfield Heights",
        "Fairfield West",
       "Fairlight",
         "Fiddletown",
         "Five Dock",
         "Flemington",
         "Forest Glen",
         "Forest Lodge",
         "Forestville",
         "Freemans Reach",
         "Frenchs Forest",
        "Freshwater"}
f_suburbs.update(requiredsuburbs)
print(f_suburbs)

#
f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
del f_suburbs["Randwick"]
del f_suburbs["Kensington"]
dic1 = {"Fairfield": 18081, "Fairfield East": 5273, "Fairfield Heights": 7517, "Fairfield West": 11575,"Fairlight": 5840, "Fiddletown": 233,"Five Dock": 9356,"Flemington": None,"Forest Glen": None, "Forest Lodge": 4583,"Forestville": 8329,"Freemans Reach": 1973,"Frenchs Forest": 13473,"Freshwater": 8866}
f_suburbs.update(dic1)
print(f_suburbs)
