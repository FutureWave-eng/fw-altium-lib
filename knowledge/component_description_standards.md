## Standardized component description list
Feel free to expand accordingly. These are guidelines, not strict rules.    
    
| Component type | Format | Example | Value parameter | Comments |
| --- | --- | --- | --- | --- |
| Zener diode | ZENER_footprint_forwardVoltage_forwardCurrent_zenerVoltage_maxReverseCurrent | ZENER_SMA_410mV_100mA_10V_30mA | Zener voltage | same as the diode, with the extra zener current parameter |
| Crystal oscillator | *XTAL*_footprint_frequency_tolerance_loadCapacitance | XTAL_IQXC42_16MHz_10ppm_9pF | frequency |  |
| TVS diode | *TVS*_footprint_reverseStandoffVoltage_peakCurrent_extraInfo | TVS_SOT323_24V_3A_CAN | usecase (CAN, USB, 3V3...) | examples for extraInfo: CAN, 5VDigital, 3V3Digital, USB,... |
| Test points | *TP_*type*_*size | TP_TH_1mm | size | Type is TH: through hole of SMT: only a pad.
For TH size is actual hole size. For SMT size is pad size |
| Transformer | *T*_Vin_Vout1_Vout2..._Vaux1*a*_Vaux2*a*... | T_2x375V_15V_15V_15Va | total input voltage | the *a* comes after auxiliary voltages to distinguish them from the secondary outputs |
| Switch & button | *SW*_type_mechanicalInfo | SW_SPST_2.54mm | latching/non-latching | Mechanical info: spacing between switches/footprint size |
| System on Module | *SOM*_moduleName_extraInfo | SOM_410357B_JTAG-UART | / | SOM are almost always unique, so a hard standard isn't really useful |
| Sensor | *SENS_*type_name | SENS_TRANSDUCER_HAIS50-P | range | range is the physical value range |
| Variable resistance | *RESV*_footprint_resistance_tolerance_power_type_extraInfo | RES_0805_10K_1%_125mW_POT | default resistance | Type can be: Potentiometer (POT), thermistor (NTC, PTC), ...Extra info can be the accuracy of the thermistor |
| Resistor | *RES*_footprint_resistance_tolerance_power | RES_0805_10K_1%_125mW | resistance |  |
| P-type MOSFET | *PMOS*_footprint_currentRating_DrainSourceVoltage | PMOS_SOT23_4.6A_60V | gate voltage |  |
| N-type MOSFET | *NMOS*_footprint_currentRating_DrainSourceVoltage | NMOS_SOT23_200mA_50V | gate voltage |  |
| Mounting point | *MP*_holesize_standoffHeight | MP_M3_13mm | standoff height |  |
| LED | *LED*_footprint_forwardVoltage_currentRating_Color | LED_2828_2V_3V2_3V2_10mA_RGB | forward voltage | for multicolor LEDs, repeat the parameter that changes, and follow the same order for the colors afterwards:_2V_3V2_3V3_10mA_RGB ==> Red = 2V, 10mA; Green = 3V2, 10mA; Blue = 3V2, 10mA |
| Jumpers | *JP_*geometry_size | JP_circle_4mm | size |  |
| Inductor | *IND*_footprint_inductance_currentRating | IND_1090_6.8µH_10.5A | inductance |  |
| IC | *IC*_type_footprint_extraInfo | IC_MCU_LQFP64_32BIT_256KB_72MHz_3V3 | custom | type examples: Latch, Bool, MCU, CANTransceiver...extra info: dependent on the type, not extremely important, space parameters with '_' |
| Fiducial | *FID_*insideDia*x*outsideDia_extraInfo | IC_1mm5_3mm | inside diameter | inside diameter is the size of the actual copper padoutside diameter is the size of the copper pad + the solder mask expansion |
| Ferrite bead | *FB*_footprint_impedance-impedanceFrequency_currentRating | FB_0402_600R-100MHz_550mA | current rating |  |
| Fuse | *F*_FuseCurrent_VoltageRating_Footprint_characteristics | F_1A_125V | Fuse current | characteristic: slow, fast, very fast... |
| External components | *EXT*_Custom | EXT_SDCARD_SDHC_10Mbps | / | These are extra components added to the ActiveBom document without a footprint (connectors on the PCB sockets, SD cars, wire crimps...) |
| Diode | *DIODE*_footprint_forwardVoltage_forwardCurrent_reverseVoltage | DIODE_SOD523_410mV_100mA_40V | current rating | Same structure as the zener, except for the zener current |
| Connectors | *CONN*_#pins*P*_#rows*x*#pinsPerRow_pinSpacing
*CONN*_usecase_extraInfo | CONN_20P_2x10_2.54mmCONN_MICRO-SD_Push-Push | usecase (STLink, USB...) or #pins | When a connector fits both categories (e.g. STLink is a 2x10 connector), use the special type, most of the time that's what they're used for |
| Common mode choke | *CHOKE*_inductance_currentRating_voltageRating_extraInfo | CHOKE_51µH_300mA_80V_CAN | inductance |  |
| Capacitor | *CAP*_footprint_capacitance_tolerance_voltage | CAP_0805_1µF_10%_25V | capacitance |  |