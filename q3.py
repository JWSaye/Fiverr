f = open("check.txt", "r")

num2words1 = {'0' : 'Zero', "1": 'One', "2": 'Two', "3": 'Three', "4": 'Four', "5": 'Five', \
            "6": 'Six', "7": 'Seven', "8": 'Eight', "9": 'Nine', "10": 'Ten', \
            "11": 'Eleven', "12": 'Twelve', "13": 'Thirteen', "14": 'Fourteen', \
            "15": 'Fifteen', "16": 'Sixteen', "17": 'Seventeen', "18": 'Eighteen', "19": 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

for line in f:
	out = ""
	data = str(line)
	datal = list(data)
	if '\n' in datal:
		datal.remove('\n')
	cents = datal[-2] + datal[-1] + "/100"
	if len(datal) > 3 or not (datal[0] == 0 and len(datal) == 4):
		i = -4
		places = {"1" : "", "10" : "", "100" : ""}
		while i >= -(len(datal)):
			try:
				if i == -4 and datal[-5] == "1":
					places["10"] = num2words1.get(datal[-5] + datal[-4])
					i = i - 1
				else:
					if i == -4:
						places["1"] = num2words1.get(datal[i])
						i = i - 1
					elif i == -5 and datal[-5] != "1":
						places["10"] = num2words2[int(datal[i])-2]
						i = i - 1
					else:
						places["100"] = num2words1.get(datal[i])
						i = i - 1
			except IndexError:
				places["1"] = num2words1.get(datal[-4])
				i = i - 1
		if places["100"] != "":
			if places["10"] in num2words2:
				out = places["100"] + " Hundred " + places["10"] + "-" + places["1"] + " And " + cents
			else:
				out = places["100"] + " Hundred " + places["10"] + " And " + cents
		elif places["10"] != "" and places["100"] == "":
			if places["10"] in num2words2:
				out = places["10"] + "-" + places["1"] + " And " + cents
			else:
				out = places["10"] + " And " + cents
		else:
			out = places["1"] + " And " + cents
		print("$" + ''.join(datal) + " is " + out)