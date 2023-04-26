all: rfsoc2x2 rfsoc4x2 zcu111 zcu208 zcu216 tarball

rfsoc2x2:
	$(MAKE) -C boards/RFSoC2x2/pynq_nco/

rfsoc4x2:
	$(MAKE) -C boards/RFSoC4x2/pynq_nco/

zcu111:
	$(MAKE) -C boards/ZCU111/pynq_nco/

zcu216:
	$(MAKE) -C boards/ZCU216/pynq_nco/

zcu208:
	$(MAKE) -C boards/ZCU208/pynq_nco/

tarball:
	tar -czvf pynq_nco.tar.gz .
