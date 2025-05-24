# Runner Tournament Manager

[**فارسی**](README-Fa.md)

A simple and practical system for running Runner Tournaments with game management, result recording, and visual/textual analysis capabilities.

## Introduction

This project is designed to manage Runner team tournaments. Simply place each team's binary files in the `Bins/` folder, define the games in `Games.txt`, and start the tournament by running `Run.sh`.

### Features

- Automated game execution between teams
- Game results recording in `wins.txt` with winner determination
- Tournament summary in `Result.txt`
- Visual analysis charts in `static/` folder

## Project Structure

```
Runner/
├── Bins/           # Team executable binaries
├── Games.txt       # Match configurations (team pairings)
├── wins.txt        # Match results (output)
├── Result.txt      # Final standings summary (output)
├── static/         # Visual analysis assets
├── run.sh          # Tournament execution script
├── Analyzer/       # Analysis and processing scripts
├── Logs/           # Complete game logs
└── README.md
```


## Usage Guide

### Team Preparation

Place team executable binaries in the `Bins/` folder. Each team must be independently executable.

### Match Configuration

In `Games.txt`, define matches using one of the following formats:

**Format 1 (Parallel Matches):**

```
Team1
Team2
Team3
Team4
```

*First match: Team1 vs Team2 
Second match: Team3 vs Team4*

**Format 2 (Sequential Matches):**
```
TeamA
TeamB
TeamC
```

*First match: Team1 vs Team2  
Second match: Winner vs Team3*

Note: Use folder names containing team binaries, not team display names.

### Running the Tournament

Execute the tournament by running:
```bash
./Run.sh
```

This will:

1. Run games according to `Games.txt`
2. Save results in wins.txt and `Result.txt`
3. Generate visual analyses in `static/`
4. Store complete game logs in `Logs/`

# Outputs

- `wins.txt`: Detailed game results with winners
- `Result.txt`: Summary of wins/losses/draws per team
- `static/`: Tournament analysis charts
- `Logs/`: Complete game logs for review

# Requirements

- Linux or macOS
- Python 3.x (with networkx, matplotlib etc.)
- Execute permission for Run.sh (chmod +x Run.sh)

# Installing Prerequisites
Install required Python packages:

```bash
pip install matplotlib networkx
```

# License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

# Contact

For issues/questions, please use the repository's Issues section.

---

[**Soroush Mazloum**](https://github.com/SoroushMazloum)

[**Saleh Hamrahi**](https://github.com/SalehHamrahi)
