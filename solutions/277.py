
with open("INPUT.TXT", "r") as f:
    a, b, c = map(int, f.read().split())

terms = []
if a != 0:
    terms.append(str(a))
    
if b != 0:
    if b == 1:
        terms.append("x")
    elif b == -1:
        terms.append("-x")
    else:
        terms.append(f"{b:+}x".replace("+", "+").replace("-", "-"))
        
if c != 0:
    if c == 1:
        terms.append("y")
    elif c == -1:
        terms.append("-y")
    else:
        terms.append(f"{c:+}y".replace("+", "+").replace("-", "-"))

if not terms:
    result = "0"
else:
    result = terms[0]
    for term in terms[1:]:
        if term.startswith("-"):
            result += term
        else:
            result += "+" + term

with open("OUTPUT.TXT", "w") as f:
    f.write(result)
