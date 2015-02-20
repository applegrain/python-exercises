__author__ = 'Applegrain'
#Lovisa Svallingson
#23 February 2015
#4
#Determine if "unknown DNA" is more similar to human DNA or mouse DNA

#Open and read the files to be used later
humanDNA = (open("humanDNA.txt", "r"))
humanText = humanDNA.read()

mouseDNA = (open("mouseDNA.txt", "r"))
mouseText = mouseDNA.read()

unknownDNA = (open("unknownDNA.txt", "r"))
unknownText = unknownDNA.read()

#calculate the hamming distance
length = len(humanText)

h_dist_human = 0.0
h_dist_mouse = 0.0

for letter in range(length):
    if humanText[letter] != unknownText[letter]:
        h_dist_human = h_dist_human + 1

for letter in range(length):
    if mouseText[letter] != unknownText[letter]:
        h_dist_mouse = h_dist_mouse + 1

#calculate similarity score for human and mouse DNA compared to the unknown DNA
sim_score_human = (length - h_dist_human) / length
sim_score_mouse = (length - h_dist_mouse) / length
print ("Human DNA similarity score: %f." % sim_score_human)
print ("Mouse DNA similarity score: %f." % sim_score_mouse)

#calculate the ID of the unknown DNA, if it's more similar to mouse or human DNA

if sim_score_human == sim_score_mouse:
    print "Identity cannot be determined."
elif sim_score_human > sim_score_mouse:
    print "The unknown DNA is more similar to human DNA."
else:
    print "The unknown DNA is more similar to mouse DNA."