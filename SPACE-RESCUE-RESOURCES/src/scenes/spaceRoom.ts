class SpaceRoom {
    constructor() {
        this.roomName = "Space Room";
    }

    display() {
        console.log(`Welcome to the ${this.roomName}`);
        // Additional code to render the room can be added here
    }

    handleUserInteraction() {
        // Code to handle user interactions in the space room
        console.log("Interacting in the Space Room...");
    }

    startOceanRoom() {
        // Logic to transition to the Ocean Room
        console.log("Transitioning to the Ocean Room...");
        // This would typically involve calling the SceneManager to switch scenes
    }
}

export default SpaceRoom;