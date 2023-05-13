# drawer-lock-system
This drawer lock system is a raspberry pi pico project using a 12V electromagnetic lock. I can say that its strength is excellent after many testing and forcing, and the code which does the logic of the system is simple but effective. One problem I have experienced is that the matrix keyboard I'm using is not a great choice for taking the pin code because it is willing to not notice a press or may detect it twice.
## Elements
- 12V adapter
- 12V solenoid lock
- rasberry pi pico
- printed circuit
- 4x4 matrix keyboard
- keep plate

![12V adapter](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/f5b90aa8-7c51-4d83-a6f2-b8afcdcd3645)![solenoid lock](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/eab4863c-76c5-4b7f-aa24-b8c48d628fe4)![rpi pico](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/43f80fe5-667f-4f40-9669-33b1c76c43e1)

## Function
The adapter gives the circuit 12V which powers the pico with 5V and the lock with 12V. The pico starts to listen the keyboard, logs the keypresses and does the logic.
```mermaid
graph LR
B[printed curcuit] --> E[lock]
Z[source] --> A[adapter] --> B[printed circuit] --> C[pico] --> B[printed circuit]
D[matrix keyboard] --> B[printed circuit]
```
## Usage
The pin code must contain 4 digits. The default pin is 0000.
### Opening the lock
- Type in the pin code.
- Confirm it with "#" to open the lock.
### Changing the pin code
- Type in the pin code.
- Get admin access with "A".
- Type in the new pin code.
> **Remember that the pin code must be 4 digits long!**
- Press "B" to confirm it and to leave admin mode, or if you are unsure, you can always press the "*" button to reset your input.
> **After every change, like getting admin access or changing the code, the lock will open for 0.05 secs to confirm it.**

> **If you want to leave admin mode without changing the code you have to press "D".**
