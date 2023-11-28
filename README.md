# Secret Santa Assignment Program

## Introduction
The Secret Santa Assignment Program is a Python script designed to facilitate the organization of Secret Santa gift exchanges in order to avoid having to draw slips manually several times (perform the process repeatedly) until you get a constellation/assignment that meets the conditions (not drawing your own partner or yourself) without having to rely on a third person to check and guarantee a random draw. It allows users to enter participant names, specify partners (who cannot be assigned as Secret Santas to each other), and even pre-determine some gift assignments. The program ensures a valid assignment for each participant, adhering to the rules of the game.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
No additional installation is required, as the script uses standard Python libraries.

### Running the Program
1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
   ```bash
   python main.py
   ```

## How to Use
1. Start the program.
2. Enter the names of participants one by one. After entering each name, you'll be prompted to enter their partner's name (if any).
3. To enter pre-determined assignments, type '1' instead of a participant's name. Then, enter the assignments in the format 'Giver > Receiver'. Type '1' again to end this mode.
4. Once all participants are entered, type 'done'.
5. The program will then display the Secret Santa assignments. Each participant can view their assignment privately.

## Contributing
This project is open for contributions. Please ensure your pull requests are concise and clear.

## License
[MIT License](LICENSE.txt)
