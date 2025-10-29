#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re

def create_drivers_from_readme():
    """
    Cria um drivers.json baseado exatamente na estrutura do README.md
    mas com links locais para /Downloads/
    """
    
    # Estrutura baseada no README.md
    printers_data = {
        "Argox": [
            {
                "modelo": "Todos",
                "versao": "2022.1",
                "download": {
                    "driver": "/Downloads/Argox/Argox_PrinterDrivers_v2022.1.exe"
                }
            }
        ],
        "Bematech": [
            {
                "modelo": "LR-1100",
                "versao": "4.2.1.0",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BemaSetup_LR_x32_v4.2.1.exe",
                    "driver_x64": "/Downloads/Bematech/BemaSetup_LR_x64_v4.2.1.exe",
                    "manual": "/Downloads/Manuals/Bematech_LR1100_Manual.pdf"
                }
            },
            {
                "modelo": "LR-2000",
                "versao": "4.2.1.0",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BemaSetup_LR_x32_v4.2.1.exe",
                    "driver_x64": "/Downloads/Bematech/BemaSetup_LR_x64_v4.2.1.exe",
                    "manual": "/Downloads/Manuals/Bematech_LR2000_Manual.pdf"
                }
            },
            {
                "modelo": "MP-2500 TH",
                "versao": "4.4.0.3",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v4.4.0.3.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v4.4.0.3.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-2500.pdf"
                }
            },
            {
                "modelo": "MP-2800 TH",
                "versao": "1.3.0.0",
                "download": {
                    "driver_x86": "/Downloads/Bematech/Bematech_MP_2800_SpoolerDrivers_v1.3.exe",
                    "driver_x64": "/Downloads/Bematech/Bematech_MP_2800_SpoolerDrivers_v1.3.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-2800.pdf"
                }
            },
            {
                "modelo": "MP-3000 TH",
                "versao": "-",
                "observacao": "Deve ser instalada com o driver Generic do Windows",
                "download": {}
            },
            {
                "modelo": "MP-4000 TH",
                "versao": "4.4.0.3",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v4.4.0.3.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v4.4.0.3.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-4000.pdf"
                }
            },
            {
                "modelo": "MP-4200 HS",
                "versao": "1.7.7.0",
                "download": {
                    "driver": "/Downloads/Bematech/Bematech MP-4200-HS_Driver_v1.7.7.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-4200 HS.pdf"
                }
            },
            {
                "modelo": "MP-4200 TH",
                "versao": "4.4.0.3",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v4.4.0.3.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v4.4.0.3.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-4200.pdf"
                }
            },
            {
                "modelo": "MP-4200 TH ADV",
                "versao": "6.0.1.0",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v6.0.1.0.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v6.0.1.0.exe"
                }
            },
            {
                "modelo": "MP-5100 TH",
                "versao": "5.0.0.4",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v5.0.0.4.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v5.0.0.4.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-5100.pdf"
                }
            },
            {
                "modelo": "MP-100S TH",
                "versao": "4.4.0.3",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v4.4.0.3.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v4.4.0.3.exe",
                    "manual": "/Downloads/Manuals/Bematech MP-100S.pdf"
                }
            },
            {
                "modelo": "PP-10",
                "versao": "6.0.1.0",
                "download": {
                    "driver_x86": "/Downloads/Bematech/BematechSpoolerDrivers_x86_v6.0.1.0.exe",
                    "driver_x64": "/Downloads/Bematech/BematechSpoolerDrivers_x64_v6.0.1.0.exe",
                    "manual": "/Downloads/Manuals/Bematech PP-10.pdf"
                }
            }
        ],
        "Control ID": [
            {
                "modelo": "PrintID",
                "versao": "1.1.10.2",
                "download": {
                    "driver": "/Downloads/PrintID/Print_iD_&_Print_iD_Touch_v1.1.10.2.exe",
                    "manual": "/Downloads/Manuals/Control iD Print iD Touch.pdf"
                }
            },
            {
                "modelo": "PrintID Touch",
                "versao": "1.1.10.2",
                "download": {
                    "driver": "/Downloads/PrintID/Print_iD_&_Print_iD_Touch_v1.1.10.2.exe",
                    "manual": "/Downloads/Manuals/Control iD Print iD.pdf"
                }
            }
        ],
        "Daruma": [
            {
                "modelo": "DR700",
                "versao": "4.0.3.1",
                "download": {
                    "driver": "/Downloads/Daruma/Daruma_700_Spooler_Driver_v4.0.3.1.exe",
                    "manual": "/Downloads/Manuals/Daruma DR700.pdf"
                }
            },
            {
                "modelo": "DR800",
                "versao": "2.0.1.7",
                "download": {
                    "driver": "/Downloads/Daruma/Daruma_800_Spooler_Driver_v2.0.1.7.exe",
                    "manual": "/Downloads/Manuals/Daruma DR800.pdf"
                }
            },
            {
                "modelo": "FS700",
                "versao": "4.0.3.1",
                "download": {
                    "driver": "/Downloads/Daruma/Daruma_700_Spooler_Driver_v4.0.3.1.exe",
                    "manual": "/Downloads/Manuals/Daruma FS700.pdf"
                }
            },
            {
                "modelo": "FS800",
                "versao": "2.0.1.7",
                "download": {
                    "driver": "/Downloads/Daruma/Daruma_800_Spooler_Driver_v2.0.1.7.exe",
                    "manual": "/Downloads/Manuals/Daruma FS800.pdf"
                }
            }
        ],
        "Dascom": [
            {
                "modelo": "DT-210",
                "versao": "1.0.0.7",
                "download": {
                    "driver": "/Downloads/Dascom/Dascom_DT-210_DT-230_Driver_v1.0.0.7.exe"
                }
            },
            {
                "modelo": "DT-230",
                "versao": "1.0.0.7",
                "download": {
                    "driver": "/Downloads/Dascom/Dascom_DT-210_DT-230_Driver_v1.0.0.7.exe",
                    "manual": "/Downloads/Manuals/Dascom_DT-230.pdf"
                }
            }
        ],
        "Diebold": [
            {
                "modelo": "TSP143MU",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe"
                }
            },
            {
                "modelo": "Mecaf Perfecta",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe",
                    "manual": "/Downloads/Manuals/Diebold Mecaf Perfecta.pdf"
                }
            },
            {
                "modelo": "IM903TT",
                "versao": "1.0.1.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_IM903TT_1.0.1.exe"
                }
            },
            {
                "modelo": "IM693H-002",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe"
                }
            },
            {
                "modelo": "IM453HU",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe"
                }
            },
            {
                "modelo": "IM433TD",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe"
                }
            },
            {
                "modelo": "IM113ID",
                "versao": "1.9.0.0",
                "download": {
                    "driver_x86": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe",
                    "driver_x64": "/Downloads/Diebold/Diebold_IM113ID_v1.2.0.10_x64.exe"
                }
            },
            {
                "modelo": "IM402TD",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Diebold/Diebold_Printers_v1.34_drv_1.9.exe"
                }
            }
        ],
        "Dimep": [
            {
                "modelo": "D-Print Dual",
                "versao": "1.9.0.0",
                "download": {
                    "driver": "/Downloads/Dimep/Dimep_D-PRINT_DUAL_v2.1.4.4.exe"
                }
            }
        ],
        "Elgin": [
            {
                "modelo": "iX(i10)",
                "versao": "1.0.2.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_iX_v1.02.exe"
                }
            },
            {
                "modelo": "i7",
                "versao": "1.7.3.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_i7_i9_v1.7.3.exe",
                    "manual": "/Downloads/Manuals/Elgin i7.pdf",
                    "utility": "/Downloads/Utilities/Elgin_i7-i8_Utility_v3.2.exe"
                }
            },
            {
                "modelo": "i8",
                "versao": "2.0.1.7",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_i8_v7.1.7.exe",
                    "manual": "/Downloads/Manuals/Elgin i8.pdf",
                    "utility": "/Downloads/Utilities/Elgin_i7-i8_Utility_v3.2.exe"
                }
            },
            {
                "modelo": "i9",
                "versao": "1.7.3.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_i7_i9_v1.7.3.exe",
                    "manual": "/Downloads/Manuals/Elgin i9.pdf",
                    "utility": "/Downloads/Utilities/Elgin_i9_Utility_v1.2.2.24.exe"
                }
            },
            {
                "modelo": "VOX",
                "versao": "1.25.0.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_VOX_V1.25.exe",
                    "manual": "/Downloads/Manuals/Elgin VOX.pdf"
                }
            },
            {
                "modelo": "VOX+",
                "versao": "1.25.0.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_VOX_V1.25.exe",
                    "manual": "/Downloads/Manuals/Elgin VOX+.pdf"
                }
            },
            {
                "modelo": "NIX",
                "versao": "3.3.0.0",
                "download": {
                    "driver": "/Downloads/Elgin/Elgin_NIX_Driver_v2.3.0.0.exe"
                }
            }
        ],
        "Epson": [
            {
                "modelo": "TM-T20",
                "versao": "5.6.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T20_v5.6.0.0.exe"
                }
            },
            {
                "modelo": "TM-T20X",
                "versao": "6.1.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T20X_v6.1.0.0.exe"
                }
            },
            {
                "modelo": "TM-T20X II",
                "versao": "6.9.1.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-20X-II_Driver_v6.9.1.0.exe"
                }
            },
            {
                "modelo": "TM-T81",
                "versao": "15.0.0.498",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T81_v15.0.0.498.exe"
                }
            },
            {
                "modelo": "TM-T88 III",
                "versao": "4.0.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T88_III_v4.exe",
                    "utility": "/Downloads/Epson/Epson_TM-T88_III_VirtualPort.exe"
                }
            },
            {
                "modelo": "TM-T88 IV",
                "versao": "4.0.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T88_IV_4.0.0.0.exe"
                }
            },
            {
                "modelo": "TM-T88 V",
                "versao": "5.6.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T88_V_v5.6.0.0.exe"
                }
            },
            {
                "modelo": "TM-T88 VI",
                "versao": "5.11.0.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T88_VI_v5.11.0.0.exe"
                }
            },
            {
                "modelo": "TM-T88 VII",
                "versao": "6.7.1.0",
                "download": {
                    "driver": "/Downloads/Epson/Epson_TM-T88_VII_Driver_v6.7.1.0.exe"
                }
            }
        ],
        "Evadin": [
            {
                "modelo": "EP-26M",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            }
        ],
        "Feasso": [
            {
                "modelo": "F-IMTER-01",
                "versao": "1.7.0.0",
                "download": {
                    "driver": "/Downloads/Feasso/Feasso_F-IMTER-01_Driver_v1.7.exe",
                    "manual": "/Downloads/Feasso/Feasso F-IMTER01.pdf"
                }
            },
            {
                "modelo": "F-IMTER-02",
                "versao": "2.0.0.0",
                "download": {
                    "driver": "/Downloads/Feasso/Feasso_F-IMTER-02_Driver_v2.0.exe",
                    "manual": "/Downloads/Feasso/Feasso F-IMTER02.pdf"
                }
            },
            {
                "modelo": "F-IMTER-03",
                "versao": "1.5.0.0",
                "download": {
                    "driver": "/Downloads/Feasso/Feasso_F-IMTER-03_Driver_v1.5.exe",
                    "manual": "/Downloads/Feasso/Feasso F-IMTER 03.pdf"
                }
            }
        ],
        "Gainscha": [
            {
                "modelo": "Todos",
                "versao": "2020.1",
                "download": {
                    "driver": "/Downloads/Gainscha/Gainscha_GPrinterDrivers_v2020.1.exe"
                }
            }
        ],
        "Gertec": [
            {
                "modelo": "G250",
                "versao": "1.1.0.0",
                "download": {
                    "driver": "/Downloads/Gertec/Driver-G250-Spooler_VCOM-v1.1.exe",
                    "manual": "/Downloads/Manuals/Gertec G250.pdf"
                }
            }
        ],
        "Jetway": [
            {
                "modelo": "JMP-100",
                "versao": "2.61J.0.0",
                "download": {
                    "driver": "/Downloads/Jetway/Jetway_JMP-100_Driver_v2.61J.exe",
                    "utility": "/Downloads/Utilities/Jetway_JMP-100_PrinterTool.zip",
                    "manual": "/Downloads/Manuals/Jetway JMP-100.pdf"
                }
            },
            {
                "modelo": "JP-500",
                "versao": "7.17.0.0",
                "download": {
                    "driver": "/Downloads/Jetway/Jetway_JP-500_Printer_Driver_v7.17.exe",
                    "utility": "/Downloads/Utilities/Jetway_JP-500_PrinterTest.zip",
                    "manual": "/Downloads/Manuals/Jetway JP-500.pdf"
                }
            },
            {
                "modelo": "JP-800",
                "versao": "2.38E.0.0",
                "download": {
                    "driver": "/Downloads/Jetway/Jetway_JP-800_PrinterDriver_v2.38E.exe",
                    "utility": "/Downloads/Utilities/Jetway_JP-800_PrinterTool.zip",
                    "manual": "/Downloads/Manuals/Jetway JP-800.pdf"
                }
            }
        ],
        "Ledtec": [
            {
                "modelo": "PMF",
                "versao": "1.0.0.0",
                "download": {
                    "driver_win7_x86": "/Downloads/Ledtec/ENGWORKS_Printers_Win7_x86.exe",
                    "driver_win7_x64": "/Downloads/Ledtec/ENGWORKS_Printers_Win7_x64.exe",
                    "driver_win10_x86": "/Downloads/Ledtec/ENGWORKS_Printers_Win8_10_x86.exe",
                    "driver_win10_x64": "/Downloads/Ledtec/ENGWORKSPrinters_Win8_10_x64.exe"
                }
            }
        ],
        "Mafra": [
            {
                "modelo": "Mafra",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            }
        ],
        "Menno": [
            {
                "modelo": "IT 250",
                "versao": "2.52",
                "download": {
                    "driver": "/Downloads/Menno/Menno_Printer_Driver_v2.52.exe"
                }
            },
            {
                "modelo": "iTD 250",
                "versao": "2.52",
                "download": {
                    "driver": "/Downloads/Menno/Menno_Printer_Driver_v2.52.exe"
                }
            },
            {
                "modelo": "LT56050",
                "versao": "2.52",
                "download": {
                    "driver": "/Downloads/Menno/Menno_Printer_Driver_v2.52.exe"
                }
            },
            {
                "modelo": "LT76050",
                "versao": "2.52",
                "download": {
                    "driver": "/Downloads/Menno/Menno_Printer_Driver_v2.52.exe"
                }
            }
        ],
        "Oi Vida": [
            {
                "modelo": "OI-58H",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            },
            {
                "modelo": "OI-1005",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            },
            {
                "modelo": "OI-1007",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            },
            {
                "modelo": "OI-1006",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            }
        ],
        "Perto": [
            {
                "modelo": "PertoPrinter",
                "versao": "2.5.0.0",
                "download": {
                    "driver": "/Downloads/PertoPrinter/PertoPrinter_Driver_2.5.exe",
                    "manual": "/Downloads/Manuals/Perto PertoPrinter.pdf"
                }
            }
        ],
        "POS": [
            {
                "modelo": "POS58",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            },
            {
                "modelo": "POS80",
                "versao": "11.3.0.0",
                "download": {
                    "driver": "/Downloads/POS/POS_Printer_Driver_Setup_v11.3.0.0.exe"
                }
            }
        ],
        "Star": [
            {
                "modelo": "BSC10",
                "versao": "2.1.0",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_BSC10_Drivers_v2.1_x86.exe",
                    "driver_x64": "/Downloads/Star/Star_BSC10_Drivers_v2.1_x64.exe"
                }
            },
            {
                "modelo": "FVP10",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "MCP20",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "MCP21",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "MCP30",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "MCP31",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "POP10",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "SP512",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "SP542",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "SP712",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "SP717",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "SP742",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "SP747",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "TSP043",
                "versao": "2.1.0",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_TSP043_x86_v2.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_TSP043_x64_v2.1.exe"
                }
            },
            {
                "modelo": "TSP143IVUE",
                "versao": "3.1.1",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.1.1.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.1.1.exe"
                }
            },
            {
                "modelo": "TSP650II",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "TSP700II",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            },
            {
                "modelo": "TSP800II",
                "versao": "3.7.2",
                "download": {
                    "driver_x86": "/Downloads/Star/Star_PrinterDrivers_x86_v3.7.2.exe",
                    "driver_x64": "/Downloads/Star/Star_PrinterDrivers_x64_v3.7.2.exe"
                }
            }
        ],
        "Sweda": [
            {
                "modelo": "SI-150",
                "versao": "1.0.0.1",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-150_SI-250_Drivers_v1.001.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-150.pdf"
                }
            },
            {
                "modelo": "SI-250",
                "versao": "1.0.0.1",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-150_SI-250_Drivers_v1.001.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-250.pdf"
                }
            },
            {
                "modelo": "SI-300L",
                "versao": "1.2.0.0",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-300_SI-300E_SI-300W_v1.2.0.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-300-L-S-W.pdf"
                }
            },
            {
                "modelo": "SI-300S",
                "versao": "1.2.0.0",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-300_SI-300E_SI-300W_v1.2.0.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-300-L-S-W.pdf"
                }
            },
            {
                "modelo": "SI-300E",
                "versao": "1.2.0.0",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-300_SI-300E_SI-300W_v1.2.0.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-300-L-S-W.pdf"
                }
            },
            {
                "modelo": "SI300W",
                "versao": "1.2.0.0",
                "download": {
                    "driver": "/Downloads/Sweda/Sweda_SI-300_SI-300E_SI-300W_v1.2.0.exe",
                    "manual": "/Downloads/Manuals/Sweda SI-300-L-S-W.pdf"
                }
            }
        ],
        "Tanca": [
            {
                "modelo": "TMP-500",
                "versao": "2.61T.0.0",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TMP-500_v2.61T.exe"
                }
            },
            {
                "modelo": "TP-450",
                "versao": "2.29E.0",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TP-450_Driver_v2.29E.exe"
                }
            },
            {
                "modelo": "TP-509",
                "versao": "2.62.0.0",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TP-509_DriverInstall_v2.62.exe",
                    "utility": "/Downloads/Utilities/Tanca_TP-509_PrinterTool_v2.22.exe"
                }
            },
            {
                "modelo": "TP-550",
                "versao": "8.1.1.2",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TP-550_Printer_Driver_v8.1.1.2.exe",
                    "utility": "/Downloads/Utilities/Tanca_TP-550_PrinterTool.exe"
                }
            },
            {
                "modelo": "TP-620",
                "versao": "6.1.0.0",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TP-620_Driver_v6.1.0.exe",
                    "utility": "/Downloads/Utilities/Tanca_TP-620_Utility_v3.2.0.1.exe"
                }
            },
            {
                "modelo": "TP-650",
                "versao": "2.11.0.0",
                "download": {
                    "driver": "/Downloads/Tanca/Tanca_TP-650_DriverInstall_v2.11.exe",
                    "utility": "/Downloads/Utilities/Tanca_TP-650_PrinterTool_1.48E.exe"
                }
            }
        ],
        "Waytec": [
            {
                "modelo": "WP-50",
                "versao": "7.17.0.0",
                "download": {
                    "driver": "/Downloads/Waytec/WayTec_WP-50_Driver_v7.17.50.exe",
                    "manual": "/Downloads/Manuals/Waytec_WP-50.pdf"
                }
            },
            {
                "modelo": "WP-100",
                "versao": "7.17.0.0",
                "download": {
                    "driver": "/Downloads/Waytec/Waytec_WP-100_Driver_v7.17.exe",
                    "manual": "/Downloads/Manuals/Waytec_WP-100.pdf"
                }
            }
        ]
    }
    
    # Utilitários por marca (baseado no README.md)
    utilities = {
        "Bematech": [
            {"name": "Utility x86", "url": "/Downloads/Utilities/Bematech_Utility_v2.9.13_x86.exe"},
            {"name": "Utility x64", "url": "/Downloads/Utilities/Bematech_Utility_v2.10.04_x64.exe"},
            {"name": "VirtualCOM", "url": "/Downloads/Bematech/Bematech_USBCOM_v4.0.2.exe"},
            {"name": "MP-2800 TH Utility", "url": "/Downloads/Utilities/Bematech_MP-2800_TH_Utility_v1.4.exe"},
            {"name": "BemaGhost", "url": "/Downloads/Utilities/BemaGhost_v1.0.exe"}
        ],
        "Control ID": [
            {"name": "Utility", "url": "/Downloads/Utilities/PrintID_Utility_v1.0.exe"}
        ],
        "Daruma": [
            {"name": "Utility", "url": "/Downloads/Utilities/Daruma_Utility_v2.20.9.exe"}
        ],
        "Diebold": [
            {"name": "Ativar Guilhotina", "url": "/Downloads/Utilities/Diebold_Ativar_Guilhotina.pdf"}
        ],
        "Dimep": [
            {"name": "VirtualCOM Windows 7 x86", "url": "/Downloads/Dimep/VirtualCOM/Dimep_VirtualCOM_v1.5.0_W7_x86.exe"},
            {"name": "VirtualCOM Windows 7 x64", "url": "/Downloads/Dimep/VirtualCOM/Dimep_VirtualCOM_v1.5.0_W7_x64.exe"},
            {"name": "VirtualCOM Windows 8 x86", "url": "/Downloads/Dimep/VirtualCOM/Dimep_VirtualCOM_v1.5.0_W8_x86.exe"},
            {"name": "VirtualCOM Windows 8 x64", "url": "/Downloads/Dimep/VirtualCOM/Dimep_VirtualCOM_v1.5.0_W8_x64.exe"}
        ],
        "Elgin": [
            {"name": "Driver Prolific Windows 11", "url": "/Downloads/Elgin/Serial_Virtual_W11_(PL2303v206).exe"},
            {"name": "Driver Prolific 2303", "url": "/Downloads/Elgin/PL2303_Driver_v1.12.0.exe"},
            {"name": "Driver Prolific 23XX", "url": "/Downloads/Elgin/PL23XX_Driver_v4.0.2.exe"}
        ],
        "Epson": [
            {"name": "Utility", "url": "/Downloads/Utilities/Epson_NetConfig_v4_9_5.exe"}
        ],
        "Menno": [
            {"name": "Utility", "url": "/Downloads/Utilities/Menno_PrinterTool_v1.56.exe"}
        ],
        "POS": [
            {"name": "Utility", "url": "/Downloads/Utilities/POS_Utilities.exe"}
        ],
        "Sweda": [
            {"name": "Utility SI-150-250", "url": "/Downloads/Utilities/Sweda_Utility_v1.524.exe"},
            {"name": "Utility SI-300", "url": "/Downloads/Utilities/Sweda_Utility_v2.03.exe"}
        ],
        "Waytec": [
            {"name": "Utility", "url": "/Downloads/Utilities/Waytec_Utility_v3.2.0.1.exe"}
        ]
    }
    
    # Ferramentas Auxiliares (seção especial)
    auxiliary_tools = [
        {
            "name": "Instalador Universal",
            "url": "/Downloads/Instalador_Universal_0.9.4.exe",
            "description": "Ferramenta para instalação automática de drivers"
        },
        {
            "name": "NetStatGUI",
            "url": "/Downloads/NetStatGUI.exe", 
            "description": "Interface gráfica para monitoramento de rede"
        }
    ]
    
    # Criar estrutura final
    final_data = {
        "printers": printers_data,
        "utilities": utilities,
        "auxiliary_tools": auxiliary_tools
    }
    
    # Salvar no diretório do projeto
    output_path = "printer-downloads/public/drivers.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ drivers.json criado com sucesso em {output_path}")
    print(f"📊 Total de marcas: {len(printers_data)}")
    
    total_models = sum(len(models) for models in printers_data.values())
    print(f"📊 Total de modelos: {total_models}")
    
    total_utilities = sum(len(utils) for utils in utilities.values())
    print(f"🔧 Total de utilitários: {total_utilities}")

if __name__ == "__main__":
    create_drivers_from_readme()