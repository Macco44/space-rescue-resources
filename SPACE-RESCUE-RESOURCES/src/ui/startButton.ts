export class StartButton {
    private buttonElement: HTMLButtonElement;

    constructor() {
        this.buttonElement = document.createElement('button');
        this.buttonElement.innerText = 'Start';
        this.buttonElement.addEventListener('click', this.handleClick.bind(this));
    }

    public render(parentElement: HTMLElement): void {
        parentElement.appendChild(this.buttonElement);
    }

    private handleClick(): void {
        // Logic to open the ocean room
        console.log('Starting the ocean room...');
        // Here you would typically call a method from SceneManager to switch to the ocean room
    }
}