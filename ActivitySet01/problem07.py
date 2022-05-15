text= "X-DSPAM-Confidence:    0.8475"
lent=len(text)
a=text.find(":")
text=text[a+1:lent]
print(float(text))