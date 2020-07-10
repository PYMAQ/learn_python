#1、两个列表可以先后相加
list1=['Joker', 'Simon', 'Ellie']
list2=['Lishka', 'Turtle']
list3=list1+list2
print(list3)
#['Joker', 'Simon', 'Ellie', 'Lishka', 'Turtle']


#2、import pprint的作用:让列表更清晰的展现出来，比如每一行展示一个list的元素
import pprint
animal_names = [
['Walter', 'Ra', 'Fluffy', 'Killer'],
['Joker', 'Simon', 'Ellie', 'Lishka', 'Fido','Lishka', 'Turtle'],
['Mr. Ed', 'Peter', 'Rocket','Star']
]
print(animal_names)
pprint.pprint(animal_names)
