import gspread
import time
from google.oauth2.service_account import Credentials
from gspread.exceptions import APIError
import json

with open("credentials.json", "r") as f:
    credentials = json.load(f)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = credentials["sheet_id"]
sh = client.open_by_key(sheet_id)
worksheet = sh.sheet1

# First value is number, second value is letter 

satisfactionMax = -float('inf')

for f in range(0, 9, 3):
    Location = [-37, -35, 15, -39, -39, 17.5, -44, -43, 20]
    while True:
        try:
            worksheet.update_cell(19, 6, Location[f])
            worksheet.update_cell(20, 6, Location[f+1])
            worksheet.update_cell(23, 6, Location[f+2])
            break
        except Exception as e:
            print("Quota exceeded. Pausing for 10 seconds...")
            time.sleep(10)

    for g in range(40, 51, 5):
        while True:
            try:
                worksheet.update_cell(18, 6, g)
                break
            except Exception as e:
                print("Quota exceeded. Pausing for 10 seconds...")
                time.sleep(10)

        for h in range(0, 4, 2):
            CatchTank = [1500, 480, 2500, 571]
            while True:
                try:
                    worksheet.update_cell(14, 2, CatchTank[h])
                    worksheet.update_cell(4, 6, CatchTank[h+1])
                    break
                except Exception as e:
                    print("Quota exceeded. Pausing for 10 seconds...")
                    time.sleep(10)

            for n in range(0, 3):
                PumpCho = ["A", "B", "C"]
                while True:
                    try:
                        worksheet.update_cell(10, 2, PumpCho[n])
                        break
                    except Exception as e:
                        print("Quota exceeded. Pausing for 10 seconds...")
                        time.sleep(10)

                for m in range(0, 2):
                    SolarMod = ["HES-260", "HES-305P"]
                    while True:
                        try:
                            worksheet.update_cell(24, 2, SolarMod[m])
                            break
                        except Exception as e:
                            print("Quota exceeded. Pausing for 10 seconds...")
                            time.sleep(10)

                    for l in range(0, 2):
                        ChemDis = ["Chlorine", "Ozone"]
                        while True:
                            try:
                                worksheet.update_cell(15, 6, ChemDis[l])
                                break
                            except Exception as e:
                                print("Quota exceeded. Pausing for 10 seconds...")
                                time.sleep(10)

                        for k in range(0, 3):
                            UVcho = ["36W", "40W", "50W"]
                            while True:
                                try:
                                    worksheet.update_cell(14, 6, UVcho[k])
                                    break
                                except Exception as e:
                                    print("Quota exceeded. Pausing for 10 seconds...")
                                    time.sleep(10)

                            if ChemDis[l] == "Chlorine":
                                x = 4
                            else:
                                x = 13
                            for j in range(1, x):
                                while True:
                                    try:
                                        worksheet.update_cell(25, 2, j)
                                        break
                                    except Exception as e:
                                        print("Quota exceeded. Pausing for 10 seconds...")
                                        time.sleep(10)

                                i = 1
                                while True:
                                    try:
                                        worksheet.update_cell(22, 2, i)
                                        
                                        power = int(worksheet.cell(26, 6).value)
                                        
                                        print(power)
                                        
                                        while True:
                                                try:
                                                    satisfactionMin = float(worksheet.cell(1, 3).value.strip('%'))/100
                                                    break
                                                except Exception as e:
                                                    print("Quota exceeded. Pausing for 10 seconds...")
                                                    time.sleep(10)

                                        if satisfactionMin > satisfactionMax:
                                                satisfactionMax = satisfactionMin
                                                battery = i
                                                panel = j
                                                UVchoFin = UVcho[k]
                                                ChemDisFin = ChemDis[l]
                                                SolarModFin = SolarMod[m]
                                                PumpChoFin = PumpCho[n]
                                                # fiveUMFin = fiveUM[b]
                                                # twoHundUMFin = twoHundUM[c]
                                                # filtLocFin = filtLoc[x]
                                                CatchTankFin = CatchTank[h]
                                                QoutFin = CatchTank[h+1]
                                                TankStor = g
                                                LocationX =Location[f]
                                                LocationY =Location[f+1]
                                                LocationZ =Location[f+2]
                                        print(
                                            battery, 
                                            panel, 
                                            satisfactionMax, 
                                            UVchoFin, 
                                            ChemDisFin, 
                                            SolarModFin, 
                                            PumpChoFin, 
                                            # fiveUMFin,
                                            # twoHundUMFin,
                                            # filtLocFin,
                                            CatchTankFin,
                                            TankStor,
                                            LocationX,
                                            LocationY,
                                            LocationZ,
                                            QoutFin
                                        )

                                        if power <= 0 or i >= j*2 or i >= 9:
                                            break
                                        
                                        i += 1
                                    
                                    except APIError as e:
                                        print("Quota exceeded. Pausing for 10 seconds...")
                                        time.sleep(10)
#
#
#---------Too many combos, too little time-------
#
# for f in range(0, 9, 3):
#     Location = [-37, -35, 15, -39, -39, 17.5, -44, -43, 20]
#     while True:
#         try:
#             worksheet.update_cell(19, 6, Location[f])
#             worksheet.update_cell(20, 6, Location[f+1])
#             worksheet.update_cell(23, 6, Location[f+2])
#             break
#         except Exception as e:
#             print("Quota exceeded. Pausing for 10 seconds...")
#             time.sleep(10)

#     for g in range(40, 51, 5):
#         while True:
#             try:
#                 worksheet.update_cell(18, 6, g)
#                 break
#             except Exception as e:
#                 print("Quota exceeded. Pausing for 10 seconds...")
#                 time.sleep(10)

#         for h in range(0, 2):
#             CatchTank = [1500, 2500]
#             while True:
#                 try:
#                     worksheet.update_cell(14, 2, CatchTank[h])
#                     break
#                 except Exception as e:
#                     print("Quota exceeded. Pausing for 10 seconds...")
#                     time.sleep(10)

#             for n in range(0, 3):
#                 PumpCho = ["A", "B", "C"]
#                 while True:
#                     try:
#                         worksheet.update_cell(10, 2, PumpCho[n])
#                         break
#                     except Exception as e:
#                         print("Quota exceeded. Pausing for 10 seconds...")
#                         time.sleep(10)

#                 for m in range(0, 2):
#                     SolarMod = ["HES-260", "HES-305P"]
#                     while True:
#                         try:
#                             worksheet.update_cell(24, 2, SolarMod[m])
#                             break
#                         except Exception as e:
#                             print("Quota exceeded. Pausing for 10 seconds...")
#                             time.sleep(10)

#                     for l in range(0, 2):
#                         ChemDis = ["Chlorine", "Ozone"]
#                         while True:
#                             try:
#                                 worksheet.update_cell(15, 6, ChemDis[l])
#                                 break
#                             except Exception as e:
#                                 print("Quota exceeded. Pausing for 10 seconds...")
#                                 time.sleep(10)

#                         for k in range(0, 3):
#                             UVcho = ["36W", "40W", "50W"]
#                             while True:
#                                 try:
#                                     worksheet.update_cell(14, 6, UVcho[k])
#                                     break
#                                 except Exception as e:
#                                     print("Quota exceeded. Pausing for 10 seconds...")
#                                     time.sleep(10)

#                             if ChemDis[l] == "Chlorine":
#                                 x = 4
#                             else:
#                                 x = 13
#                             for j in range(1, x):
#                                 while True:
#                                     try:
#                                         worksheet.update_cell(25, 2, j)
#                                         break
#                                     except Exception as e:
#                                         print("Quota exceeded. Pausing for 10 seconds...")
#                                         time.sleep(10)

#                                 i = 1
#                                 while True:
#                                     try:
#                                         worksheet.update_cell(22, 2, i)
                                        
#                                         power = int(worksheet.cell(26, 6).value)
                                        
#                                         print(power)
                                        
#                                         if power <= 0 or i >= j*2 or i >= 9:
#                                             if power <= 0:
#                                                 while True:
#                                                     try:
#                                                         satisfactionMin = float(worksheet.cell(1, 3).value.strip('%'))/100
#                                                         break
#                                                     except Exception as e:
#                                                         print("Quota exceeded. Pausing for 10 seconds...")
#                                                         time.sleep(10)
#                                                 if satisfactionMin > satisfactionMax:
#                                                     satisfactionMax = satisfactionMin
#                                                     battery = i
#                                                     panel = j
#                                                     UVchoFin = UVcho[k]
#                                                     ChemDisFin = ChemDis[l]
#                                                     SolarModFin = SolarMod[m]
#                                                     PumpChoFin = PumpCho[n]
#                                                     # fiveUMFin = fiveUM[b]
#                                                     # twoHundUMFin = twoHundUM[c]
#                                                     # filtLocFin = filtLoc[x]
#                                                     CatchTankFin = CatchTank[h]
#                                                     TankStor = g
#                                                     LocationX =Location[f]
#                                                     LocationY =Location[f+1]
#                                                     LocationZ =Location[f+2]
#                                                 print(
#                                                     battery, 
#                                                     panel, 
#                                                     satisfactionMax, 
#                                                     UVchoFin, 
#                                                     ChemDisFin, 
#                                                     SolarModFin, 
#                                                     PumpChoFin, 
#                                                     # fiveUMFin,
#                                                     # twoHundUMFin,
#                                                     # filtLocFin,
#                                                     CatchTankFin,
#                                                     TankStor,
#                                                     LocationX,
#                                                     LocationY,
#                                                     LocationZ
#                                                 )
#                                             break
                                        
#                                         i += 1
                                    
#                                     except APIError as e:
#                                         print("Quota exceeded. Pausing for 10 seconds...")
#                                         time.sleep(10)

print(
    battery, 
    panel, 
    satisfactionMax, 
    UVchoFin, 
    ChemDisFin, 
    SolarModFin, 
    PumpChoFin, 
    # fiveUMFin,
    # twoHundUMFin,
    # filtLocFin,
    CatchTankFin,
    TankStor,
    LocationX,
    LocationY,
    LocationZ
    )



            # for x in range(0, 2):
            #     filtLoc = ["Filter -> Tank", "Tank -> Filter"]
            #     while True:
            #         try:
            #             worksheet.update_cell(7, 6, filtLoc[x])
            #             break
            #         except Exception as e:
            #             print("Quota exceeded. Pausing for 10 seconds...")
            #             time.sleep(10)

                #         for c in range(0, 2):
                # twoHundUM = ["TRUE", "FALSE"]
                # while True:
                #     try:
                #         worksheet.update_cell(11, 6, twoHundUM[c])
                #         break
                #     except Exception as e:
                #         print("Quota exceeded. Pausing for 10 seconds...")
                #         time.sleep(10)

                # for b in range(0, 2):
                #     fiveUM = ["TRUE", "FALSE"]
                #     while True:
                #         try:
                #             worksheet.update_cell(10, 6, fiveUM[b])
                #             break
                #         except Exception as e:
                #             print("Quota exceeded. Pausing for 10 seconds...")
                #             time.sleep(10)