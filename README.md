from pathlib import Path

dossier = Path("./bibliotheque_shakespeare")

def trouver_piece(piece):
    for i in dossier:
        if i == piece : 
            return i
def occurence(mot, piece):
    res=0
    i = trouver_piece(piece)
    for mot2 in i:
        if mot2 == mot:
            res+=1
    return res

print(occurence("the", "bibliotheque_shakespeare/King Lear.txt"))
