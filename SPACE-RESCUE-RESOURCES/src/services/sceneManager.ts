export class SceneManager {
    private currentScene: any;

    constructor() {
        this.currentScene = null;
    }

    public switchScene(scene: any): void {
        if (this.currentScene) {
            this.currentScene.exit();
        }
        this.currentScene = scene;
        this.currentScene.enter();
    }

    public getCurrentScene(): any {
        return this.currentScene;
    }
}