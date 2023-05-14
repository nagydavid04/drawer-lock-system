# drawer-lock-system
This drawer lock system is a raspberry pi pico project using a 12V electromagnetic lock. I can say that its strength is excellent after many testing and forcing, and the code which does the logic of the system is simple but effective. One problem I have experienced is that the matrix keyboard I'm using is not a great choice for taking the pin code because it sometimes doesn't notice presses.
## Elements
- 12V adapter
- 12V solenoid lock
- rasberry pi pico
- printed circuit
- 4x4 matrix keyboard
- keep plate
- lock support

![12V adapter](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/aa1453f9-ad3a-4526-933b-9ce4eefc7b02)![solenoid lock](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/6fc3a041-b91c-4fa5-a474-0bfbae056359)![rpi pico](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/db302778-91d8-452e-8f77-4ff813a5053b)![printed_circuit](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/fec992bb-b8bd-4580-9b8b-3b4aa16f0ca4)![matrix keyboard](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/107e6e70-eb08-40db-87af-6c2227225118)![keep_plate](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/6e7c5455-6f57-4535-a22a-168cd057404d)
![lock support](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/7542c91a-d931-487f-9281-e67cbdae67f0)
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
- Press "#" to open the lock.
### Changing the pin code
- Type in the pin code.
- Get admin access with "A".
- Type in the new pin code.
> **Remember that the pin code must be 4 digits long!**
- Press "B" to confirm it and to leave admin mode, or if you are unsure, you can always press the "*" button to reset your input.
> **If you want to leave admin mode without changing the code just press "D".**

> **After every change, like getting admin access or changing the code, the lock will open for 0.05 seconds to confirm it.**
## Pictures
![IMG_0643](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/e9470b6f-2a38-4a82-9bb1-cba5f18095b7)
![IMG_0660](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/03eab610-6093-4c88-b6ef-640150eefc59)
![IMG_0657](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/3360a3ca-2413-425d-b970-a0d295cb743a)
![IMG_0675](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/b345c2d4-e761-48f8-8492-eae512ae3168)
