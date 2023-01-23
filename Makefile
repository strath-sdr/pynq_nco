all: rfsoc2x2 rfsoc4x2 zcu111

rfsoc2x2:
	$(MAKE) -C boards/RFSoC2x2/pynq_nco/

rfsoc4x2:
	$(MAKE) -C boards/RFSoC4x2/pynq_nco/

zcu111:
	$(MAKE) -C boards/ZCU111/pynq_nco/
