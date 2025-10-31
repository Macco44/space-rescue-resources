import { StartButton } from './ui/startButton';
import { SceneManager } from './services/sceneManager';
import { SpaceRoom } from './scenes/spaceRoom';
import { OceanRoom } from './scenes/oceanRoom';

class MainController {
    private sceneManager: SceneManager;
    private startButton: StartButton;

    constructor() {
        this.sceneManager = new SceneManager();
        this.startButton = new StartButton(this.handleStartClick.bind(this));
        this.initialize();
    }

    private initialize() {
        this.sceneManager.loadScene(SpaceRoom);
        this.startButton.render();
    }

    private handleStartClick() {
        this.sceneManager.loadScene(OceanRoom);
    }
}

const mainController = new MainController();