def add_contact(contacts: list[dict], new_contact):
    contacts.append(new_contact)


def show_contacts(contacts: list[dict], only_favorites=False):
    print("\nLista de contatos")
    for index, contact in enumerate(contacts):
        favorite = "⭐" if contact["favorite"] else " "
        if only_favorites:
            if contact["favorite"]:
                print(f"[{favorite}] {contact["name"]} - {contact["phone"]}")
        else:
            favorite = "⭐" if contact["favorite"] else " "
            print(f"{index + 1}. [{favorite}] {contact["name"]} - {contact["phone"]}")


def update_contact(contact: dict[str, any], updated_data: dict[str, any]):
    contact.update(updated_data)


def toggle_favorite(contact: dict[str, any]):
    contact.update({"favorite": False if contact["favorite"] else True})


def remove_contact(contacts: list[dict], contact_index: int):
    contacts.remove(contacts[contact_index])
