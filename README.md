# drawer-lock-system
This drawer lock system is a raspberry pi pico project using a 12V electromagnetic lock. I can say that its strength is excellent after many testing and forcing, and the code which does the logic of the system is simple but effective.
## Elements
- 12V adapter
- 12V solenoid lock
- rasberry pi pico
- printed circuit
- 4x4 matrix keyboard
- keep plate
- lock support

![12V adapter](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/aa1453f9-ad3a-4526-933b-9ce4eefc7b02)![solenoid lock](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/6fc3a041-b91c-4fa5-a474-0bfbae056359)![rpi pico](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/db302778-91d8-452e-8f77-4ff813a5053b)![printed_circuit](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/fec992bb-b8bd-4580-9b8b-3b4aa16f0ca4)![matrix keyboard](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/107e6e70-eb08-40db-87af-6c2227225118)![keep_plate](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/6e7c5455-6f57-4535-a22a-168cd057404d)
![lock support](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/aa50a65b-4f77-47d5-aeee-0b182eccff27)
## Operation
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
![IMG_0643](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/d6d1e50c-617e-4174-b523-c87a61fdd30b)
![IMG_0660](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/276d78a9-9090-4abb-8a37-c9f652150879)
![IMG_0657](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/b0e56d1f-ef1f-430d-810a-7b1d5faff7d1)
![IMG_0655](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/d0dba740-7aac-4df1-be2f-8c2252d8261e)
![IMG_0675](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/6a969ec4-07de-46d3-ba75-a1abefa76a0d)
![IMG_0688](https://github.com/nagydavid04/drawer-lock-system/assets/132921246/03fadebd-1981-4aa5-92d5-879a5544d172)
