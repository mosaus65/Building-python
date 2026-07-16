team_stats = {}

while True:
    team1 = input("\nEnter home team name: ")
    score1 = int(input(f"Enter {team1}'s score: "))

    team2 = input("Enter away team name: ")
    score2 = int(input(f"Enter {team2}'s score: "))

    # Initialize teams if not already in dictionary
    if team1 not in team_stats:
        team_stats[team1] = {"wins": 0, "goals": 0}
    if team2 not in team_stats:
        team_stats[team2] = {"wins": 0, "goals": 0}

    # Add goals
    team_stats[team1]["goals"] += score1
    team_stats[team2]["goals"] += score2

    # Decide winner
    if score1 > score2:
        print(f"{team1} wins! 🏆")
        team_stats[team1]["wins"] += 1
    elif score2 > score1:
        print(f"{team2} wins! 🏆")
        team_stats[team2]["wins"] += 1
    else:
        print("It's a draw! 🤝")

    print(f"Final score: {team1} {score1} - {score2} {team2}")

    again = input("Add another match? (yes/no): ")
    if again.lower() != "yes":
        break

# 📊 Show stats
print("\n--- Team Stats ---")
for team, stats in team_stats.items():
    print(f"{team} | Wins: {stats['wins']} | Goals: {stats['goals']}")