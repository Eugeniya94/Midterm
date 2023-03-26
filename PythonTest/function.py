import file_operation
import Note
import ui

number = 6  # минимальная длина текста заметки


def addNote():
    note = ui.createNote(number)
    array = file_operation.readFile()
    for notes in array:
        if Note.Note.getId(note) == Note.Note.getId(notes):
            Note.Note.setId(note)
    array.append(note)
    file_operation.writeFile(array, 'a')
    print('Заметка добавлена...')


def showNote(text):
    logic = True
    array = file_operation.readFile()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.mapNote(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.getId(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.getDate(notes):
                print(Note.Note.mapNote(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def refactorNote(text):
    id = input('Введите id необходимой заметки: ')
    array = file_operation.readFile()
    logic = True
    for notes in array:
        if id == Note.Note.getId(notes):
            logic = False
            if text == 'edit':
                note = ui.createNote(number)
                Note.Note.setTiitle(notes, note.getTitle())
                Note.Note.setBody(notes, note.getBody())
                Note.Note.setDate(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'showNote':
                print(Note.Note.mapNote(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.writeFile(array, 'a')