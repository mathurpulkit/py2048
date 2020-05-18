<HTML>
    <p>This is the Python Terminal implementation of the popular game 2048.</p>
    <p>It gets the size of board and winning number from the user as a command line argument. </p>
    <p>and then the user can play using WASD or the arrow keys(Works only on windows).</p>
    <p>If the user passes a winning number that isn't a power of 2, then it rounds it off using logarithm and round.</p>
    <p>Tested on Windows 10 PyCharm Terminal and Ubuntu 19(sudo access required for keyboard library).</p>
    <p>Keyboard library has been shipped with the code as Ubuntu isn't able to recognise installation of keyboard even after using pip.</p>
    <p>Keyboard library has to be separately installed using pip.</p>
    <p>To play the game, run the following on terminal:</p>
    <p>Windows: python game.py --n boardsize --w winningnumber</p>
    <p>Ubuntu: sudo python3 game.py --n boardsize --w winningnumber</p>
    <p>If the winning number specified isn't an integral power of 2, it rounds it off to the nearest power.</p>
    <h1>Screenshots</h1>
    <h2>Windows:</h2>
    <img src="ss1.png" width="640" height="360" alt="Screenshot">
    <img src="ss2.png" width="640" height="360" alt="Screenshot">
    <img src="ss3.png" width="640" height="360" alt="Screenshot">
    <img src="ss4.png" width="640" height="360" alt="Screenshot">
    <h2>Ubuntu:</h2>
    <img src="ssl1.png" width="640" height="360" alt="Screenshot">
    <img src="ssl2.png" width="640" height="360" alt="Screenshot">
    <img src="ssl3.png" width="640" height="360" alt="Screenshot">
    <img src="ssl4.png" width="640" height="360" alt="Screenshot">
    <h3>Known Issues:</h3>
<p>1. Sometimes the keypresses might be displayed when using Ubuntu Terminal.</p>
<p>2. The keypresses displayed in Ubuntu might also get printed in between the gameboard.</p>
</HTML>