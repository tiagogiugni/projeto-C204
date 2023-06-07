from pprintpp import pprint as pp

class Pokemon(object):
    def __init__(self, name):
        self.name = name


class PokedexDAO(object):
    def __init__(self):
        self.pokemons = []

    def create_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def read_all_nodes(self):
        return self.pokemons

    def delete(self, pokemon_name):
        self.pokemons = [pokemon for pokemon in self.pokemons if pokemon.name != pokemon_name]

    def delete_all_nodes(self):
        self.pokemons = []

    def search_pokemon(self, index):
        for pokemon in self.pokemons:
            if self.get_pokemon_index(pokemon) == index:
                return pokemon
        return None

    def get_pokemon_index(self, pokemon):
        return self.pokemons.index(pokemon) + 1

def divider():
    print('\n' + '-' * 80 + '\n')


dao = PokedexDAO()

while True:
    option = input('\n1. Adicionar um pokemon na Pokedex\n2. Remover um Pokemon\n3. Procurar um pokemon\n4. Ver quais pokemons estão cadastrados\n5. Deletar tudo\n')

    if option == '1':
        name = input('  Nome: ')
        pokemon = Pokemon(name)
        dao.create_pokemon(pokemon)
        divider()

    elif option == '2':
        name = input('  Nome: ')
        dao.delete(name)
        divider()

    elif option == '3':
        index = int(input('  Posição: '))
        pokemon = dao.search_pokemon(index)
        if pokemon:
            print(f"Pokemon achado na posição {index}: {pokemon.name}")
        else:
            print("Pokemon não achado na posição especificada.")
        divider()

    elif option == '4':
        all_nodes = dao.read_all_nodes()
        for node in all_nodes:
            print(node.__dict__)
        divider()

    elif option == '5':
        dao.delete_all_nodes()
        divider()

    else:
        break

