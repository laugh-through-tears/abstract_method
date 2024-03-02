try:
    from abstract_method.personal_assistant_bot.classes.record import Record
    from abstract_method.personal_assistant_bot.classes.addressbook import AddressBook
    from abstract_method.personal_assistant_bot.classes.notes import Notes
    from abstract_method.personal_assistant_bot.functions.functions import make_menu
    from abstract_method.personal_assistant_bot.functions.make_header import make_header
    from abstract_method.personal_assistant_bot.functions.sort import sort
    from abstract_method.personal_assistant_bot.settings.settings import addressbook_filename, notes_filename
except ModuleNotFoundError:
    from personal_assistant_bot.classes.record import Record
    from personal_assistant_bot.classes.addressbook import AddressBook
    from personal_assistant_bot.classes.notes import Notes
    from personal_assistant_bot.functions.functions import make_menu
    from personal_assistant_bot.functions.make_header import make_header
    from personal_assistant_bot.functions.sort import sort
    from personal_assistant_bot.settings.settings import addressbook_filename, notes_filename

from colorama import init, Fore
from abc import ABC, abstractmethod

init(autoreset=True)


class AbstractChat(ABC):
    @classmethod
    @abstractmethod
    def message(cls):
        pass


class MainMenu(AbstractChat):
    @classmethod
    def message(cls):
        return ('''
1. About Bot Helper
2. Hello, User!
3. Use Records
4. Use Notes
5. Sort Files in Folder
6. Exit

Please, input your choice: ''')


class ChoiceOneOne(AbstractChat):
    @classmethod
    def message(cls):
        make_header("ABOUT BOT HELPER")
        print("\nI'm a great bot and I will facilitate your work, now I will describe what I can do\n"
              "I can work with contact: add, edit, remove contact's phone, email, birthday, address.\nAlso "
              "I can work with your notes: add, edit, remove, show note or all notes, find and sort notes.\n"
              "And finally, I have very useful function - sort, it helps you to sort all your files in "
              "some directory. \nWhere do you want to start?")

        input("\nPress Enter to continue...")


class ChoiceOneTwo(AbstractChat):
    @classmethod
    def message(cls):
        make_header("HELLO, USER!")
        print('\nHello! How are you today? Are you ready to work?')

        input("\nPress Enter to continue...")


class RecordMenu(AbstractChat):
    @classmethod
    def message(cls):
        return ('''
1. Show all Records
2. Find Records
3. Show Records with birthday in N days
4. Add Record
5. Edit Record
6. Delete Record
7. Save AddressBook
8. Exit to previous menu

Please, input your choice: ''')


class ChoiceTwoOne(AbstractChat):
    @classmethod
    def message(cls):
        make_header("SHOW ALL RECORDS")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        book.iterator()
        input("\nPress Enter to continue...")


class ChoiceTwoTwo(AbstractChat):
    @classmethod
    def message(cls):
        make_header("FIND RECORDS")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        find_string = input("\nPlease input Name of record, which you want find: ")
        find_result = AddressBook()
        find_result = book.find_record(find_string)

        if find_result:
            print("")
            book.find_record(find_string).iterator_simple()
        else:
            print(Fore.RED + f"\nI can`t find any matches with '{find_string}'")

        input("\nPress Enter to continue...")


class ChoiceTwoThree(AbstractChat):
    @classmethod
    def message(cls):
        make_header("N DAYS FROM BIRTHDAY")

        days_to_search = input("\nPlease input number of days to search: ")
        print("")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        book.find_birthdays(days_to_search).iterator()

        input("\nPress Enter to continue...")


class ChoiceTwoFour(AbstractChat):
    @classmethod
    def message(cls):
        make_header("ADD RECORD")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        name = input("\nPlease enter the name: ")
        new_record = Record(name)

        while True:
            phone = input("Please enter the phone: ")
            try:
                new_record.add_phone(phone)
            except ValueError:
                print(Fore.RED + 'Incorrect number format. Please enter a 10-digit number.')
            else:
                break

        while True:
            email = input("Please enter the email: ")
            try:
                new_record.add_email(email)
            except ValueError:
                print(Fore.RED + 'Incorrect email format. Please enter email like user@example.com.')
            else:
                break

        address = input("Please enter the address: ")
        new_record.add_address(address)

        while True:
            birthday = input("Please enter the date of birth in format DD/MM/YYYY: ")
            try:
                new_record.add_birthday(birthday)
            except ValueError:
                print(Fore.RED + 'Waiting format of date - DD/MM/YYYY. Reinput, please.')
            else:
                break

        book.add_record(new_record)
        print(Fore.GREEN + "\nRecord added successful!\n")

        book.appruve_record(new_record)

    input("\nPress Enter to continue...")


class ChoiceTwoFive(AbstractChat):
    @classmethod
    def message(cls):
        make_header("EDIT RECORD")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        book.edit_record()

        input("\nPress Enter to continue...")


class ChoiceTwoSix(AbstractChat):
    @classmethod
    def message(cls):
        make_header("DELETE RECORD")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        contact_name = input("\nPlease enter contact name you need to delete: ")
        print("")

        book.delete(contact_name)

        input("\nPress Enter to continue...")


class ChoiceTwoSeven(AbstractChat):
    @classmethod
    def message(cls):
        make_header("SAVE ADDRESSBOOK")
        book = AddressBook()
        book = AddressBook.read_contacts_from_file(addressbook_filename)
        book.write_contacts_to_file(addressbook_filename)

        print(Fore.GREEN + "\nAddressBook saved successful!")

        input("\nPress Enter to continue...")


class ChoiceOneFive(AbstractChat):
    @classmethod
    def message(cls):
        make_header("SORT FILES IN FOLDER")
        print(Fore.RED + "\nCarefully! Files will be sorted! You won't be able to find them in your usual place!")

        folder = input("\nPlease input folder name or press Enter to exit: ")

        if not folder:
            pass
        else:
            sort(folder)

            print(Fore.GREEN + f"\nFiles and folders in {folder} sorted successful!")

            input("\nPress Enter to continue...")
