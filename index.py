"""
[x] add new contact (name, phone, email and favorite)
[x] list all contacts
[x] update a contact
[x] mark and mark off favorite
[x] list all favorite contacts
[x] delete a contact
"""

from functions import (
    add_contact,
    show_contacts,
    update_contact,
    toggle_favorite,
    remove_contact,
)

contacts = []

while True:
    print("\nGerenciador de contatos")
    print("1. Adicionar um novo contato")
    print("2. Listar contatos")
    print("3. Atualizar um contato")
    print("4. Marcar como favorito ou desmarcar")
    print("5. Listar todos os favoritos")
    print("6. Remover um contato")
    print("7. Sair")

    option = int(input("Digite uma opção: "))

    if option == 1:
        new_contact = {"favorite": False}
        new_contact.update({"name": input("Digite o nome do contato: ")})
        new_contact.update({"phone": input("Digite o telefone do contato: ")})
        new_contact.update({"email": input("Digite o email do contato: ")})

        add_contact(contacts, new_contact)

    elif option == 2:
        show_contacts(contacts)

    elif option == 3:
        show_contacts(contacts)

        contact_index = (
            int(input("Digite o número do contato que você deseja atualizar: ")) - 1
        )

        if contact_index >= 0 and contact_index < len(contacts):
            contact_selected = contacts[contact_index]
            new_info = {}

            new_info.update(
                {
                    "name": input(f"Nome [{contact_selected["name"]}]:")
                    or contact_selected["name"]
                }
            )
            new_info.update(
                {
                    "phone": input(f"Telefone [{contact_selected["phone"]}]:")
                    or contact_selected["phone"]
                }
            )
            new_info.update(
                {
                    "email": input(f"Email [{contact_selected["email"]}]:")
                    or contact_selected["email"]
                }
            )

            update_contact(contact_selected, new_info)
        else:
            print("Contato inválido!")

    elif option == 4:
        show_contacts(contacts)

        contact_index = (
            int(
                input(
                    "Digite o número do contato para marcar ou desmarcar como favorito: "
                )
            )
            - 1
        )

        if contact_index >= 0 and contact_index < len(contacts):
            toggle_favorite(contacts[contact_index])
        else:
            print("Contato inválido!")

    elif option == 5:
        show_contacts(contacts, True)

    elif option == 6:
        show_contacts(contacts)

        contact_index = int(input("Digite o número do contato que deseja remove: ")) - 1

        if contact_index >= 0 and contact_index < len(contacts):
            remove_contact(contacts, contact_index)
        else:
            print("Contato inválido!")
    else:
        break

print("Programa finalizado")
