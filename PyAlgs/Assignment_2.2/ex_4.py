def main():
    # List of tuples containing first and last names
    people = [
        ('Alice', 'Jones'),
        ('Bob', 'Smith'),
        ('Carol', 'Jones'),
        ('David', 'Brown'),
        ('Eve', 'Jones'),
        ('Frank', 'Davis'),
        ('Grace', 'Jones'),
        ('Hank', 'Wilson')
    ]
    
    # Use filter to locate the tuples containing the last name Jones
    jones_people = filter(lambda person: person[1] == 'Jones', people)
    
    print("People with last name 'Jones':")
    for person in jones_people:
        print(person)

if __name__ == '__main__':
    main()
