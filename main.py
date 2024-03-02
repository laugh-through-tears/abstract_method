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
import abstract_consol

init(autoreset=True)


def main():

    while True:

        make_header("MAIN MENU")
        choice1 = input(abstract_consol.MainMenu.message())

        if choice1 == "1":

            abstract_consol.ChoiceOneOne.message()

        elif choice1 == "2":

            abstract_consol.ChoiceOneTwo.message()

        elif choice1 == "3":

            switcher = True

            while switcher:

                book = AddressBook()
                book = AddressBook.read_contacts_from_file(addressbook_filename)
                record_menu = abstract_consol.RecordMenu.message()

                make_header("ADDESSBOOK MENU")
                choice2 = input(record_menu)

                if choice2 == "1":

                    abstract_consol.ChoiceTwoOne.message()

                elif choice2 == "2":

                    abstract_consol.ChoiceTwoTwo.message()

                elif choice2 == "3":

                    abstract_consol.ChoiceTwoThree.message()

                elif choice2 == "4":

                    abstract_consol.ChoiceTwoFour.message()

                elif choice2 == "5":

                    abstract_consol.ChoiceTwoFive.message()

                elif choice2 == "6":

                    abstract_consol.ChoiceTwoSix.message()

                elif choice2 == "7":

                    abstract_consol.ChoiceTwoSeven.message()

                elif choice2 == "0":
                    switcher = False

        elif choice1 == "4":
            notes = Notes().load_from_file(notes_filename)
            make_menu(notes)

        elif choice1 == "5":

            abstract_consol.ChoiceOneFive.message()

        elif choice1 == "0":
            break


if __name__ == '__main__':
    main()
