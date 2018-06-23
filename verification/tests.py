init_code = """
if not "Transport" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Transport'?")

Transport = USER_GLOBAL['Transport']

if not "Airplane" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Airplane'?")

Airplane = USER_GLOBAL['Airplane']

if not "Train" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Train'?")

Train = USER_GLOBAL['Train']

if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not issubclass(Airplane, Transport):
    raise Warning("Airplane should be the subclass of the Transport")

if not issubclass(Train, Transport):
    raise Warning("Train should be the subclass of the Transport")

if not issubclass(Car, Transport):
    raise Warning("Car should be the subclass of the Transport")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

person_1 = Airplane("John")
person_2 = Train("Bob")
person_3 = Car("Alice")

person_1.travel("1000 km") == """1. John go to the airport
2. John fly by the airplane: 1h and 7m
3. John walk to the nearest bar"""
    
person_2.travel("450 miles") == """1. Bob go to the train station
2. Bob travel by the train: 6h and 2m
3. Bob walk to the nearest bar"""
    
person_3.travel("5290 km") == """1. Alice go to the garage
2. Alice ride by the car: 52h and 54m
3. Alice walk to the nearest bar"""


TESTS = {
    "Travelers": [
        prepare_test(middle_code="person_1 = Airplane('Carl')",
                     test="person_1.travel('1000 km')",
                     answer="""1. Carl go to the airport
2. Carl fly by the airplane: 1h and 7m
3. Carl walk to the nearest bar"""),

        prepare_test(middle_code="person_2 = Train('Miranda')",
                     test="person_2.travel('450 miles')",
                     answer="""1. Miranda go to the train station
2. Miranda travel by the train: 6h and 2m
3. Miranda walk to the nearest bar"""),

        prepare_test(middle_code="person_3 = Car('Mark')",
                     test="person_3.travel('5290 km')",
                     answer="""1. Mark go to the garage
2. Mark ride by the car: 52h and 54m
3. Mark walk to the nearest bar"""),

        prepare_test(middle_code="person_4 = Airplane('Helen')",
                     test="person_4.travel('1615 miles')",
                     answer="""1. Helen go to the airport
2. Helen fly by the airplane: 2h and 53m
3. Helen walk to the nearest bar"""),

        prepare_test(middle_code="person_5 = Train('Rick')",
                     test="person_5.travel('1285 km')",
                     answer="""1. Rick go to the train station
2. Rick travel by the train: 10h and 43m
3. Rick walk to the nearest bar"""),

        prepare_test(middle_code="person_6 = Car('Morty')",
                     test="person_6.travel('386 km')",
                     answer="""1. Morty go to the garage
2. Morty ride by the car: 3h and 52m
3. Morty walk to the nearest bar""")
    ]

}
