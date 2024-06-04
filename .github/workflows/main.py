from bakery import assert_equal
from drafter import *
from dataclasses import dataclass


@dataclass
class State:
    name: str
    age: int
    weight: int
    height_inches: int
    bench: int
    squat: int
    deadlift: int
    user_bulking: bool
    users_split: str
    goals: list[str]

@route
def index(state) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        Image('https://st3.depositphotos.com/4259987/12661/i/450/depositphotos_126613676-stock-photo-weightlifter-preparing-for-training.jpg'),
    Button('Training', choose_training),
    Button('Diet Tracker', diet_edited),
    ])
    

'The following routes correspond to the "Diet Tracker" Button'




@route
def diet_edited(state: State)-> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        
        'Name:',
        state.name,
        
        'Age:',
        state.age,
        
        'Weight (lbs):',
        state.weight,
        
        
        'Height (Inches):',
        state.height_inches,
        
        'Goals:',
        *state.goals,
        Button('fix info', enter_info),
        
        ' ',
        Button('Diet Guide', diet_guide),
        ' ',
        Button('return', index)   
     
    ])

@route
def diet_guide(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        
        'Check this box if you are bulking. Leave it Blank if you are cutting.',
        CheckBox('bulking', state.user_bulking),
        Button('macro nutrients', macro_nutrients),
        Button('Return', diet_edited)
        
        ])

@route
def macro_nutrients(state, bulking: bool) -> Page:        
        if bulking:
            url = Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ71e-AiGEZj5BfRMOS_pCERkH1JpIwknvU9C446SPS0g&s")
        else:
            url = Image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp6QgUzkAPctifjU1Z1lawa5HFm_ceAQWzF5CyQsq8sw&s")
        
        state.user_bulking = bulking
        return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        url, Button('return', diet_guide)
        ])

@route
def enter_info(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        "Name:",
        state.name,
        TextBox('newName',' '),
        
        'Age:',
        state.age,
        TextBox('newAge', ' '),
        
        'Weight (lbs):',
        state.weight,
        TextBox('newWeight', ' '),
        
        'Height (Inches):',
        state.height_inches,
        TextBox('newHeight', ' '),
        
        'Goals:',
        *state.goals,
        TextBox('newGoals', ' '),
        TextBox('newGoals1', ' '),
        
        Button('save', set_the_input)
           ])
    
@route
def set_the_input(state: State, newName, newWeight, newAge, newHeight, newGoals, newGoals1) -> Page:
    state.name = newName
    state.age = newAge
    state.weight = newWeight
    state.height_inches = newHeight
    state.goals = [newGoals, newGoals1]
    return diet_edited(state)


'Diet Tracking ends'

'The following routes correspond to the "Training" Button'

@route
def choose_training(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        
        'Click your preferred split : arnold or push pull legs',
        Button('arnold', arnold_page),
        Button('Push Pull Legs', PPL),
        Button('enter pr', enter_pr),
        ' ',
        Button('Return', index)
        ])

def remove_spaces(user_word: str)-> str:
    no_spaces = user_word.replace(' ','')
    return no_spaces.lower()

@route
def training(state: State, choosen_split: str) -> Page:
    if remove_spaces(choosen_split) == "arnold":
        return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
                '**For all exercises train to failure unless you are injured**',
        Image("https://www.schwarzenegger.com/assets/images/img-3.jpg"),

        '''Monday:
           Chest And Back''',
        '''Tuesday:
           Arms And Shoulders''',
        '''Wednesday:
           Legs''',
        '''Thursday:
           Chest And Back''',
        '''Friday:
           Arms And Shoulders''',
        '''Saturday
           Legs''',
        '''Sunday:
           
           Rest''',
        Button('Chest And Back', chest_back),
        Button('Arms', arms),
        Button('legs', legs),
        ' ',
        Button('Return', choose_training) 
           ])
    elif remove_spaces(choosen_split) == "pushpulllegs":
        return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
                '**For all exercises train to failure unless you are injured**',
                Image("https://thegymgoat.com/wp-content/uploads/2022/03/Chris-Bumstead-workout-and-diet.jpeg"),

        '''Monday:
           Push''',
        '''Tuesday:
           Pull''',
        '''Wednesday:
           Legs''',
        '''Thursday:
           Push''',
        '''Friday:
           Pull''',
        '''Saturday
           Legs''',
        '''Sunday:
           
           Rest''',
        Button('Push', Push),
        Button('pull', Pull),
        Button('legs', legs_ppl),
        ' ',
        Button('enter pr', enter_pr),
        Button('Return', choose_training)
           ])
    else:
        return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'Something went wrong. Please return and re-enter your split',
         Image('https://t3.ftcdn.net/jpg/01/12/43/90/360_F_112439022_Sft6cXK9GLnzWjjIkVMj2Lt34RcKUpxm.jpg'),
         Button('Return', choose_training)
        ])

    
@route
def PPL(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
                '**For all exercises train to failure unless you are injured**',
        Image("https://thegymgoat.com/wp-content/uploads/2022/03/Chris-Bumstead-workout-and-diet.jpeg"),

        '''Monday:
           Push''',
        '''Tuesday:
           Pull''',
        '''Wednesday:
           Legs''',
        '''Thursday:
           Push''',
        '''Friday:
           Pull''',
        '''Saturday
           Legs''',
        '''Sunday:
           
           Rest''',
        Button('Push', Push),
        Button('pull', Pull),
        Button('legs', legs_ppl),
        ' ',
        Button('Return', choose_training)  
           ])
@route
def Push(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'C H E S T:',
        '''Dumbell Press 5-10 reps                                                                                               

        ''',
        'Incline Dumbell Press 5-10 reps',
        'Dips 5-10 reps | High-to-low cable flies 7-12 reps',
        
        'S H O U L D E R S:',
        '''Dumbell Shoulder Press 5-10 reps '''                                                                                             ,
        'Lateral Raises 5-10 reps',
        'Rear Delt Flies 5-10 reps | Rear Delt Row 5-10 reps',
        
        'T R I C E P S:',
        'Straight Bar Push Downs 6-8 reps',
        'Cross Body Push Downs 6-8 reps',
        
        Button('Return', PPL)
        
           ])

@route
def Pull(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'B A C K:',
        'Bent Over Rows 5-7 reps (Dumbell or Barbell)',
        'Lat Pull downs (Upper Back Biased) 5-7 reps',
        ' ',
        'B I C E P S:',
        'Hammer Curls 6-10 reps',
        'Preacher Curls 6-10 reps',        
        Button('Return', PPL)
        
           ])

@route
def legs_ppl(state: State)-> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'Q U A D S:',
        'Squats 5-7 reps',
        'Quad Extensions 5-10 reps',
        
        'H A M S T R I N G S:',
        'Romanian Deadlifts 5-7 reps',
        'Hamstring Curls 5-10 reps',
        
        'G L U T E S:',
        'Hip Thrusts 5-7 reps',
        'Hip Abductors 5-10 reps',
        
        'A B S:',
        'Machine Curls',
        Button('Return', PPL)
        ])
    
    
    
@route
def arnold_page(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
                '**For all exercises train to failure unless you are injured**',
        Image("https://www.schwarzenegger.com/assets/images/img-3.jpg"),
        '''Monday:
           Chest And Back''',
        '''Tuesday:
           Arms And Shoulders''',
        '''Wednesday:
           Legs''',
        '''Thursday:
           Chest And Back''',
        '''Friday:
           Arms And Shoulders''',
        '''Saturday
           Legs''',
        '''Sunday:
           
           Rest''',
        Button('Chest And Back', chest_back),
        Button('Arms', arms),
        Button('legs', legs),
        ' ',
        Button('Return', choose_training) 
        
           ])



@route
def chest_back(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'C H E S T:',
        '''Dumbell Press 5-10 reps                                                                                               

        ''',
        'Incline Dumbell Press 5-10 reps',
        'Dips 5-10 reps | High-to-low cable flies 7-12 reps',
        
        'B A C K:',
        'Bent Over Rows 5-7 reps (Dumbell or Barbell)',
        'Lat Pull downs (Upper Back Biased) 5-7 reps',
        Button('Return', arnold_page)
        
           ])
@route
def arms(state: State)-> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'S H O U L D E R S:',
        '''Dumbell Shoulder Press 5-10 reps '''                                                                                             ,
        'Lateral Raises 5-10 reps',
        'Rear Delt Flies 5-10 reps | Rear Delt Row 5-10 reps',
        ' ',
        'B I C E P S:',
        'Hammer Curls 6-10 reps',
        'Preacher Curls 6-10 reps',
        ' ',
        'T R I C E P S:',
        'Straight Bar Push Downs 6-8 reps',
        'Cross Body Push Downs 6-8 reps',
        Button('Return', arnold_page)
           ])

@route
def legs(state: State)-> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        'Q U A D S:',
        'Squats 5-7 reps',
        'Quad Extensions 5-10 reps',
        
        'H A M S T R I N G S:',
        'Romanian Deadlifts 5-7 reps',
        'Hamstring Curls 5-10 reps',
        
        'G L U T E S:',
        'Hip Thrusts 5-7 reps',
        'Hip Abductors 5-10 reps',
        
        'A B S:',
        'Machine Curls',
        Button('Return', arnold_page)
        
        
        
           ])


@route
def enter_pr(state: State) -> Page:
    return Page(state, [
        '▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
        "Bench Press:",
        state.bench,
        TextBox('newBench',' '),
        
        'Squat:',
        state.squat,
        TextBox('newSquat', ' '),
        
        'Deadlift:',
        state.deadlift,
        TextBox('newDeadlift', ' '),
        
        Button('save', set_the_pr),
        ' ',
        Button('return', choose_training)
        
        ])



@route
def set_the_pr(state: State, newBench, newSquat, newDeadlift) -> Page:
    state.bench = newBench 
    state.squat = newSquat
    state.deadlift = newDeadlift
    return enter_pr(state)
    

start_server(State(' ',
                   ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '))
'UNIT TESTS'

'INDEX'
assert_equal(
 index(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              Image(url='https://st3.depositphotos.com/4259987/12661/i/450/depositphotos_126613676-stock-photo-weightlifter-preparing-for-training.jpg',
                    width=None,
                    height=None),
              Button(text='Training', url='/choose_training'),
              Button(text='Diet Tracker', url='/diet_edited')]))

'TRAINING'
assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if text box left empty'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if arnold entered'
assert_equal(
 training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' '), ' arnold'),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              '**For all exercises train to failure unless you are injured**',
              Image(url='https://www.schwarzenegger.com/assets/images/img-3.jpg', width=None, height=None),
              'Monday:\n           Chest And Back',
              'Tuesday:\n           Arms And Shoulders',
              'Wednesday:\n           Legs',
              'Thursday:\n           Chest And Back',
              'Friday:\n           Arms And Shoulders',
              'Saturday\n           Legs',
              'Sunday:\n           \n           Rest',
              Button(text='Chest And Back', url='/chest_back'),
              Button(text='Arms', url='/arms'),
              Button(text='legs', url='/legs'),
              ' ',
              Button(text='Return', url='/choose_training')]))

'if chest and back pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if arms pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if legs pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if push pull legs typed in text box'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if push pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if pull pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if legs pressed'

assert_equal(
 choose_training(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Type in your preferred split : arnold or push pull legs',
              TextBox(name='choosen_split', kind='text', default_value=' '),
              Button(text='view split', url='/training'),
              Button(text='enter pr', url='/enter_pr'),
              ' ',
              Button(text='Return', url='/')]))

'if diet tracker pressed'

assert_equal(
 diet_edited(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Name:',
              ' ',
              'Age:',
              ' ',
              'Weight (lbs):',
              ' ',
              'Height (Inches):',
              ' ',
              'Goals:',
              ' ',
              Button(text='fix info', url='/enter_info'),
              ' ',
              Button(text='Diet Guide', url='/diet_guide'),
              ' ',
              Button(text='return', url='/')]))

'if fix info clicked'
assert_equal(
 diet_edited(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Name:',
              ' ',
              'Age:',
              ' ',
              'Weight (lbs):',
              ' ',
              'Height (Inches):',
              ' ',
              'Goals:',
              ' ',
              Button(text='fix info', url='/enter_info'),
              ' ',
              Button(text='Diet Guide', url='/diet_guide'),
              ' ',
              Button(text='return', url='/')]))

'if diet guide clicked'

assert_equal(
 diet_edited(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Name:',
              ' ',
              'Age:',
              ' ',
              'Weight (lbs):',
              ' ',
              'Height (Inches):',
              ' ',
              'Goals:',
              ' ',
              Button(text='fix info', url='/enter_info'),
              ' ',
              Button(text='Diet Guide', url='/diet_guide'),
              ' ',
              Button(text='return', url='/')]))

'if macro nutrients clicked'

assert_equal(
 macro_nutrients(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=[' ', ' ']), True),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=True,
                 users_split=' ',
                 goals=[' ', ' ']),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              Image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ71e-AiGEZj5BfRMOS_pCERkH1JpIwknvU9C446SPS0g&s',
                    width=None,
                    height=None),
              Button(text='return', url='/diet_guide')]))

assert_equal(
 diet_edited(State(name=' ', age=' ', weight=' ', height_inches=' ', bench=' ', squat=' ', deadlift=' ', user_bulking=' ', users_split=' ', goals=' ')),
 Page(state=State(name=' ',
                 age=' ',
                 weight=' ',
                 height_inches=' ',
                 bench=' ',
                 squat=' ',
                 deadlift=' ',
                 user_bulking=' ',
                 users_split=' ',
                 goals=' '),
     content=['▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀  P O W E R - F I T N E S S  ▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀',
              'Name:',
              ' ',
              'Age:',
              ' ',
              'Weight (lbs):',
              ' ',
              'Height (Inches):',
              ' ',
              'Goals:',
              ' ',
              Button(text='fix info', url='/enter_info'),
              ' ',
              Button(text='Diet Guide', url='/diet_guide'),
              ' ',
              Button(text='return', url='/')]))






