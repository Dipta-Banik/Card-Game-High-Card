# -*- coding: utf-8 -*-
"""Card Game: High Card.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mw1tMt7S5ndKMwEMq1nfkenqj3i-1FF8
"""

import matplotlib.pyplot as plt
import random


suits = {
    "♠": "black",
    "♥": "red",
    "♦": "red",
    "♣": "black"
}

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def draw_card(ax, player, rank, suit):
    ax.set_aspect('equal')
    ax.set_axis_off()


    ax.add_patch(plt.Rectangle((0, 0), 1, 1.5, color='lightgrey', ec='black', lw=2))


    ax.add_patch(plt.Rectangle((0, 0), 1, 1.5, color='white', ec='black', lw=2))


    ax.text(0.5, 1.1, rank, fontsize=20, ha='center', va='center', color=suits[suit])
    ax.text(0.5, 1.4, suit, fontsize=30, ha='center', va='center', color=suits[suit])
    ax.text(0.5, -0.2, player, fontsize=14, ha='center', va='center')

def pick_a_card():
    card_suit = random.choice(list(suits.keys()))
    card_rank = random.choice(ranks)
    return card_rank, card_suit

def play_round(round_num):
    print(f"\nRound {round_num}:")
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    players = ["Player 1", "Player 2"]
    round_winner = None
    for i, player in enumerate(players):
        rank, suit = pick_a_card()
        draw_card(axs[i], player, rank, suit)
        if i == 0:
            rank_p1 = rank
        else:
            rank_p2 = rank


    rank_values = {rank: i for i, rank in enumerate(ranks)}
    if rank_values[rank_p1] > rank_values[rank_p2]:
        print("Player 1 wins the round!")
        round_winner = 1
    elif rank_values[rank_p1] < rank_values[rank_p2]:
        print("Player 2 wins the round!")
        round_winner = 2
    else:
        print("It's a tie!")

    plt.show()
    return round_winner

def play_game():
    num_rounds = int(input("Enter the number of rounds: "))
    player1_score = 0
    player2_score = 0

    for round_num in range(1, num_rounds + 1):
        result = play_round(round_num)
        if result == 1:
            player1_score += 1
        elif result == 2:
            player2_score += 1

    print("\nGame over!")
    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player1_score < player2_score:
        print("Player 2 wins the game!")
    else:
        print("It's a tie!")


play_game()

