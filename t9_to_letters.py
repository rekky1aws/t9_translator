correspondance = [
	["a", "b", "c"], ["d", "e", "f"],
	["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
	["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]
]

def from_t9 (str) :
	pass

def to_t9 (input_str) :
	input_str = input_str.lower()
	splitted_str = []
	result = ""
	for l in input_str :
		splitted_input_str.append(l)
		for i in range(len(correspondance)) :
			if (l in correspondance[i]) :
				for j in range(correspondance[i].index(l) + 1) :
					result = f"{result}{i + 2}"
	return result
	pass

print("coucou", to_t9("coucou"))