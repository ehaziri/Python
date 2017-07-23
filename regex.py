import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]


#1
# print(get_matching_words(r"[a-zA-Z0-9]*v[a-zA-Z0-9]*"))

#2
# print(get_matching_words(r"[a-zA-Z0-9]*ss[a-zA-Z0-9]*"))

#3
# print(get_matching_words(r"[a-zA-Z0-9]*e$"))

#4
# print(get_matching_words(r"[a-zA-Z0-9]*b.b[a-zA-Z0-9]*"))

#5
# print(get_matching_words(r".*b.+b.*"))

#6
# print(get_matching_words(r".*b.*b.*"))

#7
# print(get_matching_words(r".*a{1}.*e{1}.*i{1}.*o{1}.*u{1}.*"))
