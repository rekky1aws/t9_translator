correspondance = [
	["a", "b", "c"], ["d", "e", "f"],
	["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"],
	["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]
]

def from_t9 (input_str) :
	nb_p = 0
	last_pressed = int(input_str[1]) - 2
	print(last_pressed)
	result = ""
	for l in input_str :
		if int(l) - 2 == last_pressed:
			if nb_p <= len(correspondance[last_pressed]) :
				nb_p += 1
			else :
				result += correspondance[last_pressed][nb_p - 1]
				nb_p = 0
		else :
			result += correspondance[last_pressed][nb_p - 1]
			nb_p = 0
			last_pressed = int(l) - 2
	return result
	pass

def to_t9 (input_str) :
	input_str = input_str.lower()
	splitted_str = []
	result = ""
	for l in input_str :
		splitted_str.append(l)
		for i in range(len(correspondance)) :
			if (l in correspondance[i]) :
				for j in range(correspondance[i].index(l) + 1) :
					result = f"{result}{i + 2}"
	return result

print("coucou", to_t9("coucou"))
print(from_t9(to_t9("coucou")))