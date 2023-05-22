<img src="strathsdr_banner.png" width="100%">

# PYNQ NCO Overlay
This repository hosts a Numerically Controlled Oscillator (NCO) overlay compatible with [PYNQ image v2.7](https://github.com/Xilinx/PYNQ/releases) and greater for the following development boards:
* [ZCU208](https://www.xilinx.com/products/boards-and-kits/zcu208.html),
* [ZCU216](https://www.xilinx.com/products/boards-and-kits/zcu216.html),
* [ZCU111](https://www.xilinx.com/products/boards-and-kits/zcu111.html),
* [RFSoC4x2](https://www.xilinx.com/support/university/xup-boards/RFSoC4x2.html),
* [RFSoC2x2](https://www.xilinx.com/support/university/xup-boards/RFSoC2x2.html).

## Quick Start
Follow the instructions below to install the project now. **You will need to give your board access to the internet**.
* Power on your RFSoC development board with an SD Card containing a fresh PYNQ v2.7 image or greater.
* Navigate to Jupyter Labs by opening a browser (preferably Chrome) and connecting to `http://<board_ip_address>:9090/lab`.
* We need to open a terminal in Jupyter Lab. Firstly, open a launcher window as shown in the figure below:

<p align="center">
  <img src="./open_jupyter_launcher.jpg" width="50%" height="50%" />
</p>

* Now open a terminal in Jupyter as illustrated below:

<p align="center">
  <img src="./open_terminal_window.jpg" width="50%" height="50%" />
</p>

Run the code below in the jupyter terminal to install the project.

```sh
pip3 install https://github.com/strath-sdr/pynq_nco/releases/download/v1.0.2/pynq_nco.tar.gz
```

This repository currently has no Jupyter notebooks. See https://github.com/strath-sdr/RFSoC-Book for compatible notebooks.

## Using the Project Files
The following software is required to use the project files in this repository.
- Vivado Design Suite 2020.2

### Vivado
This project can be built with Vivado from the command line. Open Vivado 2020.2 and execute the following into the tcl console:
```sh
cd /<repository-location>/boards/<board-name>/pynq_nco/
```
Now that we have moved into the correct directory, make the Vivado project by running the make commands below sequentially.
```sh
make block_design
make bitstream
```

Alternatively, you can run the entire project build by executing the following into the tcl console:
```sh
make all
```

## License 
[BSD 3-Clause](../../blob/master/LICENSE)
