__author__ = 'Applegrain'

print ("Europe - facts")


#get input from user
new_country = str(raw_input("What country are you from?"))
new_leader = str(raw_input("Who is the president or prime minister if your country?"))
new_time = str(raw_input("And for how long has this person been the president or prime minister?"))



#add info to the dictionary
dictionary = {'Stefan Lofven': ['Sweden','5 months'], 'Angela Merkel': ['Germany','8 years']}
dict_file = open("country_facts.txt", "w")
dict_file = open("country_facts.txt", "r+")
dict_file.write("Name\t\tCountry\t\tTime\n")

dict_file_str = dict_file.read()
print dict_file_str

dictionary[new_leader] = [new_country, new_time]

for name, facts in dictionary.iteritems():
    entry = name + "\t\t" + facts[0] + "\t\t" + facts[1] + "\n"
    dict_file.write(entry)


#method to get the values of the ouput
class Leader:
    def __init__(self, leader):
        self.name = leader

    def display(self):
        print self.name, "has been the political leader of", self.country, "since", self.time, "and seems to be enjoyoing it."


lofven = Leader("Stefan Lofven")
lofven.name = ("Stefan Lofven")
lofven.country = "Sweden"
lofven.time = "5 months"

merkel = Leader("Angela Merkel")
merkel.name = ("Angela Merkel")
merkel.country = ("Germany")
merkel.time = ("a long time")


new_leader_ob = Leader(new_leader)
new_leader_ob.name = (new_leader)
new_leader_ob.country = (new_country)
new_leader_ob.time = (new_time)

lofven.display()
merkel.display()
new_leader_ob.display()

