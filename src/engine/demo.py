from table import HoldemTable

holdem_game = HoldemTable(num_players=5, deck_type='full')
holdem_game.add_to_hand(1, ['Td', 'Ts'])
holdem_game.add_to_hand(2, ['Ad', 'As'])
holdem_game.next_round()
holdem_game.next_round()
print(holdem_game.view_table())
print(holdem_game.simulate())