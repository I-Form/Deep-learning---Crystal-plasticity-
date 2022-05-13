# -*- coding:utf-8 -*-
import os, sys, shutil
def alter(file,old_str,new_str):
    """
    
    :param file:
    :param old_str:
    :param new_str:
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

if __name__ == "__main__":
    for i in range(200):
        shutil.copyfile("generator.json","generator_"+str(i)+".json")
        file = "generator_"+str(i)+".json"
        alter(file, "@Grain_Info@", "Grain_Info_"+str(i))
        alter(file, "@3D@", "3D_" + str(i))
        alter(file, "@OriMap@", "OriMap_" + str(i))
        alter(file, "@phase@", "phase_"+str(i))
        command = "D:/DREAM3D-6.5.133-Win64/PipelineRunner -p D:/1_Abaqus_Temp/Steel_PH/Test_Dream3D/generator_" + str(i)+".json"
        os.system(command)