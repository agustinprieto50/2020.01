class Administration:
    listEmployee = {}

    def add_employee(self, employee):
        legajo = len(self.listEmployee)
        self.listEmployee[legajo] = employee
        return


if __name__ == '__main__':
    adm = Administration()
    adm.add_employee({'name': "Claudio", 'surname': "Pico",
                     'age': 30, 'phone': 155858585})
    adm.add_employee({'name': "Nicolas", 'surname': "Pico",
                     'age': 30, 'phone': 155858585})
    print(adm.listEmployee)
