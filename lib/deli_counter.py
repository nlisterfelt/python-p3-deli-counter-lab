katz_deli=[]
def line(katz_deli):
    if(len(katz_deli)==0):
        print('The line is currently empty.')
    else:
        line_string=''
        for person in katz_deli:
            line_string += f' {katz_deli.index(person)+1}. {person}'
        print(f'The line is currently:{line_string}')

def take_a_number(katz_deli, person_name):
    katz_deli.append(person_name)
    print(f'Welcome, {person_name}. You are number {katz_deli.index(person_name)+1} in line.')

def now_serving(katz_deli): 
    if(len(katz_deli)!=0):
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.pop(0)
    else:
        print('There is nobody waiting to be served!')

take_a_number(katz_deli,'nicole')
take_a_number(katz_deli,'al')
line(katz_deli)
now_serving(katz_deli)
line(katz_deli)