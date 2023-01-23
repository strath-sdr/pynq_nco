## RFSoC2x2 Constraints

# An off-chip clock to handle clock conversion
set_property PACKAGE_PIN G13 [get_ports "sys_clk_clk_p"]
set_property IOSTANDARD DIFF_HSTL_I_12 [get_ports "sys_clk_clk_p"]