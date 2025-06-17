class Room2 {
    constructor(game) {
        this.game = game;
        this.completionScore = 0;
        this.currentLevel = 1;
        this.maxLevels = 3;
        this.isActive = false;
        this.servers = [];
        this.loadBalance = 50;
        this.trafficLevel = 1;
    }

    async init() {
        console.log('Room 2 (Cloud Scale) initializing...');
        this.render();
        this.setupGame();
    }

    render() {
        const container = document.getElementById('room-content');
        container.innerHTML = `
            <div class="room-container p-6 fade-in">
                <div class="text-center mb-6">
                    <i class="bi bi-cloud text-6xl text-green-500 animate-pulse"></i>
                    <h2 class="text-3xl font-bold mt-4 text-green-400">CLOUD INFRASTRUCTURE SCALING</h2>
                    <p class="text-gray-300 mt-2">Manage server load and auto-scaling policies!</p>
                </div>
                
                <div class="status-grid grid grid-cols-3 gap-4 mb-6">
                    <div class="status-card bg-blue-900 p-4 rounded text-center">
                        <i class="bi bi-server text-blue-400 text-2xl"></i>
                        <p class="text-sm text-blue-200">Server Load</p>
                        <p id="server-load" class="text-2xl font-bold text-blue-100">50%</p>
                        <p class="text-xs text-blue-300">Balanced</p>
                    </div>
                    <div class="status-card bg-green-900 p-4 rounded text-center">
                        <i class="bi bi-speedometer text-green-400 text-2xl"></i>
                        <p class="text-sm text-green-200">Performance</p>
                        <p id="performance-score" class="text-2xl font-bold text-green-100">${Math.round(this.completionScore)}%</p>
                        <p class="text-xs text-green-300">Optimal</p>
                    </div>
                    <div class="status-card bg-purple-900 p-4 rounded text-center">
                        <i class="bi bi-layers text-purple-400 text-2xl"></i>
                        <p class="text-sm text-purple-200">Traffic Level</p>
                        <p id="traffic-level" class="text-2xl font-bold text-purple-100">${this.trafficLevel}</p>
                        <p class="text-xs text-purple-300">Moderate</p>
                    </div>
                </div>

                <div class="game-area bg-gray-800 p-6 rounded-lg">
                    <div id="cloud-game" class="relative bg-gray-900 rounded" style="height: 400px; border: 2px solid #10b981;">
                        <div class="text-center text-white p-8">
                            <h3 class="text-xl mb-4">Cloud Infrastructure Dashboard</h3>
                            <p class="mb-4">Click "Start Scaling" to begin managing your cloud infrastructure!</p>
                        </div>
                    </div>
                    
                    <div class="controls mt-4 text-center">
                        <button id="start-scaling" class="bg-green-600 hover:bg-green-700 px-6 py-2 rounded mr-2">
                            <i class="bi bi-play-fill"></i> Start Scaling
                        </button>
                        <button id="add-server" class="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded mr-2">
                            <i class="bi bi-plus-circle"></i> Add Server
                        </button>
                        <button id="complete-room" class="bg-purple-600 hover:bg-purple-700 px-6 py-2 rounded mr-2">
                            <i class="bi bi-check-circle"></i> Complete
                        </button>
                        <button id="exit-room" class="bg-red-600 hover:bg-red-700 px-6 py-2 rounded">
                            <i class="bi bi-x-circle"></i> Exit
                        </button>
                    </div>
                </div>
            </div>
        `;

        this.setupEventListeners();
    }

    setupEventListeners() {
        const startBtn = document.getElementById('start-scaling');
        const addServerBtn = document.getElementById('add-server');
        const completeBtn = document.getElementById('complete-room');
        const exitBtn = document.getElementById('exit-room');

        if (startBtn) {
            startBtn.addEventListener('click', () => this.startScaling());
        }
        if (addServerBtn) {
            addServerBtn.addEventListener('click', () => this.addServer());
        }
        if (completeBtn) {
            completeBtn.addEventListener('click', () => this.completeRoom());
        }
        if (exitBtn) {
            exitBtn.addEventListener('click', () => this.exitRoom());
        }
    }

    setupGame() {
        console.log('Cloud scaling game setup complete');
    }

    startScaling() {
        this.isActive = true;
        this.updateDisplay();
        console.log('Cloud scaling started');
    }

    addServer() {
        if (this.isActive) {
            this.servers.push({ id: Date.now(), load: 0 });
            this.completionScore += 10;
            this.updateDisplay();
        }
    }

    updateDisplay() {
        const loadElement = document.getElementById('server-load');
        const performanceElement = document.getElementById('performance-score');
        const trafficElement = document.getElementById('traffic-level');

        if (loadElement) {
            loadElement.textContent = `${this.loadBalance}%`;
        }
        if (performanceElement) {
            performanceElement.textContent = `${Math.round(this.completionScore)}%`;
        }
        if (trafficElement) {
            trafficElement.textContent = this.trafficLevel.toString();
        }
    }

    completeRoom() {
        this.isActive = false;
        const message = `Cloud infrastructure scaled successfully! Performance: ${Math.round(this.completionScore)}%`;
        this.game.roomCompleted(message);
    }

    exitRoom() {
        this.cleanup();
        this.game.gameOver('Cloud scaling session ended.');
    }

    cleanup() {
        this.isActive = false;
        this.servers = [];
        console.log('Room 2 cleaned up');
    }
}

// Register globally and export
window.Room2 = Room2;
export { Room2 as Room1 };
