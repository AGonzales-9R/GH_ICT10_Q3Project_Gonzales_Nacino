# ICT 10 Seatwork #2: Intramurals Team Checker
from pyscript import display, document

def intrams(e):
    document.getElementById('output').innerHTML=" "
    online = document.querySelector('input[name="online"]:checked').value
    med = document.querySelector('input[name="med"]:checked').value
    gr = document.getElementById('gr').value
    sec = document.getElementById('sec').value

    if online == 'yes' and med == 'yes' and sec == 'eme':
        display(f'Congratulations! You are part of the Yellow Tigers!', target='output')
        document.getElementById("image").innerHTML = "<img src='yellow_tigers.jpg' height='300px' width='350px'>"

    elif online == 'yes' and med == 'yes' and sec == 'ruby':
        display(f'Congratulations! You are part of the Blue Bears!', target='output')
        document.getElementById("image").innerHTML = "<img src='blue_bears.jpg' height='300px' width='350px'>"

    elif online == 'yes' and med == 'yes' and sec == 'saph':
        display(f'Congratulations! You are part of the Green Hornets!', target='output')
        document.getElementById("image").innerHTML = "<img src='green_hornets.jpg' height='300px' width='350px'>"

    elif online == 'yes' and med == 'yes' and sec == 'tpz':
        display(f'Congratulations! You are part of the Red Bulldogs!', target='output')
        document.getElementById("image").innerHTML = "<img src='red_bulldogs.jpg' height='300px' width='350px'>"


    elif online == 'no' and med == 'no':
        display(f'Please register online and get your medical clearance from the clinic.', target='output')

    elif online == 'yes' and med == 'no':
        display(f'Please get your medical clearance from the clinic.', target='output')

    elif online == 'no' and med == 'yes':
        display(f'Please register online.', target='output')

    else:
        display(f'Please answer the form above.', target='output')

def players(e):
    document.getElementById('listOfPlayers').innerHTML=" "
    fill = document.querySelector('input[name="form"]:checked').value
    gr = document.getElementById('gr').value
    sec = document.getElementById('sec').value

    if fill == 'yes' and sec == 'eme':
        display(f'''
        Here is your lineup of players:
        Soriano
        Sumulong
        Pascual
        Guevarra
        Dalisay
        Quinto
        Maliksi
        Bermudez
        Mangubat
        Espiritu
        ''', target='listOfPlayers')

    elif fill == 'yes' and sec == 'ruby':
        display(f'''
        Here is your lineup of players:
        Nardo 
        Dimaculangan 
        Reyes 
        Cabatingan 
        Sangreo
        Canete 
        Galang 
        Jamet 
        Yao 
        Villegas''', target='listOfPlayers')

    elif fill == 'yes' and sec == 'saph':
        display(f'''
        Here is your lineup of players:
        Aseo
        Hizon
        Yao
        Mendoza
        Ngo
        Ko
        Intalan
        Uy
        Rivera
        Lagman
        ''', target='listOfPlayers')

    elif fill == 'yes' and sec == 'tpz':
        display(f'''
        Here is your lineup of players:
        Espina
        Enriquez
        Abdullah
        Arias
        Garcia
        Yao
        Escobar
        Choi
        Ong
        Cajucom''', target='listOfPlayers')

    else:
        display(f'Please answer the form above.', target='listOfPlayers')




