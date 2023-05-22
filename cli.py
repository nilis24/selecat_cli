import questionary
from pyfiglet import Figlet
from clint.textui import colored

assignatures = {
    "Català": "llca",
    "Castellà": "lles",
    "Anglès": "angl",
    "Història": "hist",
    "Matemàtiques": "mate",
    "Física": "fisi",
    "Tecnologia": "tecn"
}

mesos = {
    "Juny": "j",
    "Setembre": "s"
}

solucionari = {
    True: "p",
    False: "l"
}

f = Figlet(font='slant')
print(colored.red(f.renderText('Selecat CLI')))


assignatura_u = questionary.select(
    "Quina assignatura de selectivitat vols repassar?",
    choices=["Català", "Castellà", "Anglès", "Història", "Matemàtiques", "Física", "Tecnologia"],
).ask()

mes_u = questionary.select(
    "Quin mes?",
    choices=["Juny", "Setembre"],
).ask()

any_u = questionary.text("Quin any (2000 - 2022)?").ask()

solucionari_u = questionary.confirm("Vols el solucionari?").ask()

link = f"https://www.selecat.cat/view.php?p=pau_{assignatures[assignatura_u]}{str(any_u)[-2:]}{mesos[mes_u]}{solucionari[solucionari_u]}"

print("\n" + colored.blue(">>> ") + "\033[1m" + link + "\033[0m" + colored.blue(" <<<"))