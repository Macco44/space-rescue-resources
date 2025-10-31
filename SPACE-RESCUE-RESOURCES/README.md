# SPACE-RESCUE-RESOURCES

## Project Overview
SPACE-RESCUE-RESOURCES is an interactive game that allows players to explore different rooms, starting from a space-themed room and transitioning to an ocean-themed room. The game is built using TypeScript and follows a modular architecture for easy maintenance and scalability.

## Project Structure
```
SPACE-RESCUE-RESOURCES
├── src
│   ├── mainController.ts       # Main entry point for the application
│   ├── index.ts                # Bootstraps the application
│   ├── scenes
│   │   ├── spaceRoom.ts        # Represents the initial space room
│   │   └── oceanRoom.ts        # Represents the ocean room
│   ├── ui
│   │   └── startButton.ts      # UI component for the start button
│   └── services
│       └── sceneManager.ts     # Manages scene transitions
├── package.json                # npm configuration file
├── tsconfig.json               # TypeScript configuration file
└── README.md                   # Project documentation
```

## Getting Started
To get started with the project, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd SPACE-RESCUE-RESOURCES
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   ```
   npm start
   ```

## Features
- Interactive scenes that allow players to navigate between different environments.
- A start button to initiate the game.
- Modular design for easy updates and feature additions.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.