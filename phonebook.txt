phone_book={}
def add_contact():
    name=input("enter the name")
    phone_num=int(input("enter the number"))
    phone_book[name]=phone_num
    print()
    print()
    print("------contact saved successfully----")
    print(phone_book)
add_contact()

def read_contact():
    search_name=input("enter the searching number:").strip().lower()
    if search_name in phone_book.keys():
        print()
        print()
        print(f"the number for {search_name.capitilize()} is : {phone_num}")
    else:
        print("----the contact is not available")
read_contact()

def update_contact():
    update_name=input("enter the name").strip().lower()
    update_number=int(input("enter the number to update:".strip()))
    phone_book[update_name] = update_number
    print()
    print()
    print("---contact saved successfully")
update_contact()


def main():
    while(True):
        print("choose the task from the below options")
        print("""
              1.add contact
              2.read contact
              3.update contact
              4.delete contact""")
        choice=int(input("enter the choice"))
        if choice==1:
            add_contact()
        elif choice==2:
            read_contact()
        elif choice==3:
            update_contact()
        else:
            break
if __name__=='__main__':
    main()