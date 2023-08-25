<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web-based Maze Game</title>
  <script src="https://cdn.jsdelivr.net/npm/phaser@3.60.0/dist/phaser.min.js"></script>
</head>
<body>
  <script>
    const config = {
      type: Phaser.AUTO,
      width: 1500,
      height: 800,
      scene: {
        preload: preload,
        create: create,
        update: update
      },
      physics: {
        default: 'arcade',
        arcade: {
          gravity: { y: 0 },
          debug: false
        }
      }
    };

    const game = new Phaser.Game(config);
    let player;
    let moving = false; // Track if the player is moving
    let velocityX = 0;
    let velocityY = 0;

    function preload() {
      this.load.image('player', 'b.png');
    }

    function create() {
      player = this.physics.add.sprite(200, 200, 'player');
      player.setBounce(1); // Full bounce when hitting walls
      player.setCollideWorldBounds(true); // Prevent the player from going out of the screen
      cursors = this.input.keyboard.createCursorKeys();
    }

    function update() {
      if (!moving) { // If not moving, check for arrow key press
        if (cursors.left.isDown) {
          moving = true;
          velocityX = -160;
          player.setAngle(90); // Rotate player sprite
        } else if (cursors.right.isDown) {
          moving = true;
          velocityX = 160;
          player.setAngle(-90); // Rotate player sprite
        } else if (cursors.up.isDown) {
          moving = true;
          velocityY = -160;
          player.setAngle(0); // Reset player rotation
        } else if (cursors.down.isDown) {
          moving = true;
          velocityY = 160;
          player.setAngle(180); // Rotate player sprite
        }
      }

      player.setVelocity(velocityX, velocityY);

      if (player.body.blocked.left || player.body.blocked.right) {
        moving = false;
        velocityX = -velocityX; // Reverse the horizontal velocity
        player.setVelocityX(velocityX);
      }

      if (player.body.blocked.up || player.body.blocked.down) {
        moving = false;
        velocityY = -velocityY; // Reverse the vertical velocity
        player.setVelocityY(velocityY);
      }
    }
  </script>
</body>
</html>
