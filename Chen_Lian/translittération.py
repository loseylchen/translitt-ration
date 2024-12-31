# Mapping pour la translittération
transliteration_map = {
    'Α': 'A', 'α': 'a',
    'Β': 'V', 'β': 'v',
    'Γ': 'G', 'γ': 'g',
    'Δ': 'D', 'δ': 'd',
    'Ε': 'E', 'ε': 'e',
    'Ζ': 'Z', 'ζ': 'z',
    'Η': 'Ī', 'η': 'ī',
    'Θ': 'Th', 'θ': 'th',
    'Ι': 'I', 'ι': 'i',
    'Κ': 'K', 'κ': 'k',
    'Λ': 'L', 'λ': 'l',
    'Μ': 'M', 'μ': 'm',
    'Ν': 'N', 'ν': 'n',
    'Ξ': 'X', 'ξ': 'x',
    'Ο': 'O', 'ο': 'o',
    'Π': 'P', 'π': 'p',
    'Ρ': 'R', 'ρ': 'r',
    'Σ': 'S', 'σ': 's', 'ς': 's',
    'Τ': 'T', 'τ': 't',
    'Υ': 'Y', 'υ': 'y',
    'Φ': 'F', 'φ': 'f',
    'Χ': 'Ch', 'χ': 'ch',
    'Ψ': 'Ps', 'ψ': 'ps',
    'Ω': 'Ō', 'ω': 'ō'
}

def transliterate(text):
    return ''.join(transliteration_map.get(char, char) for char in text)

# Chemin vers le fichier d'entrée
input_file_path = '/Users/lianchen/Desktop/INALCO/2024-2025课程/Ecriture et multilingue/作业1月交/2步/wiki_ecriture_grec3.txt'

# Lire le texte depuis le fichier
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    text = input_file.read()
    transliterated_text = transliterate(text)

# Chemin vers le fichier de sortie
output_file_path = '/Users/lianchen/Desktop/INALCO/2024-2025课程/Ecriture et multilingue/作业1月交/2步/wiki_ecriture_grec3_translit.txt'

# Écrire le texte translittéré dans le nouveau fichier
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(transliterated_text)
