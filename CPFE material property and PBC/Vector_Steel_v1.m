%Before run this script, delete first 2 lines of the original "Rolled.csv"
%file.
for i = 0:2
grain_name = ['Grain_Info_',num2str(i),'.csv'];
Info = csvread(grain_name, 2, 0);  
Grain_number = importdata('Grain_Info.csv');
Eulerangle = Info(:,[6,7,8]);
% Eulerangle(1,;)=[];
% Eulerangle(2,;)=[];
Phases = Info(:,11);
% Phases(1,;)=[];
% Phases(2,;)=[];
cs = crystalSymmetry('6mm');
oM = ipfHSVKey(cs);
vector_name = ['Vectors_',num2str(i),'.inp'];
file = fopen(vector_name,'w');
for n=1:Grain_number
    RotM = eul2rotm (Eulerangle (n,:));
    ori = orientation('Euler',57.3*Eulerangle (n,1)*degree,57.3*Eulerangle (n,2)*degree,57.3*Eulerangle (n,3)*degree);
    rgb = oM.orientation2color(ori);
    rgb = fix(255*rgb/4)*4; 
    hex = dec2hex(rgb);
    str1 = num2str (hex (1,:));
    str2 = num2str (hex (2,:));
    str3 = num2str (hex (3,:));
    str = [str1,str2,str3];
    v1 = RotM(:,1);
    v2 = RotM(:,2);
    v3 = RotM(:,3);
    %**********************************************
    ebsdphase_no = Phases(n);
    if ebsdphase_no == 1 %BCC
    %define M1-M6 here
     M1 = ['*Material, name=Grain_Mat',num2str(n),'\r\n']; 
     Mplus = ['**',str,'\r\n'];
     M2 = '*DEPVAR\r\n';
     M3 = '180,\r\n'; 
     M4 = '*USER MATERIAL, CONSTANTS=161, UNSYMM\r\n'; 
     M5 = ['262000.,    150000.,      112000.,     0.,      0.,      0.,      0.,   0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      1.,      1.,      1.,      1.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n'];
     line1 = [' ',num2str(round((v1(1)),3)),'   ,    ',num2str(round((v1(2)),3)),',    ',num2str(round((v1(3)),3)),',     1.00000    ,     0.00000    ,     0.00000\r\n'];
     line2 = [' ',num2str(round((v2(1)),3)),'   ,    ',num2str(round((v2(2)),3)),',    ',num2str(round((v2(3)),3)),',     0.00000    ,     0.00000    ,     1.00000\r\n'];
    M6 = ['50.,   0.001,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '20.,  740.,    466.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,     10.,   1e-05,      0.,      0.,      0.,      0.,      0.\r\n    0.,    0.,      0.,      0.,      0.,      0.,      0.,      0. \r\n'];
                 fprintf(file,M1);
                 fprintf(file,Mplus);
                 fprintf(file,M2);
                 fprintf(file,M3);
                 fprintf(file,M4);
                 fprintf(file,M5);
                 fprintf(file,line1);
                 fprintf(file,line2) ;
                 fprintf(file,M6);
    end
    
    if ebsdphase_no == 2 %FCC
    %define M1-M6 here
     M1 = ['*Material, name=Grain_Mat',num2str(n),'\r\n']; 
     Mplus = ['**',str,'\r\n'];
     M2 = '*DEPVAR\r\n';
     M3 = '180,\r\n'; 
     M4 = '*USER MATERIAL, CONSTANTS=161, UNSYMM\r\n'; 
     M5 = ['204600.,    137700,      126200.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      1.,      1.,      1.,      1.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n'];
     line1 = [' ',num2str(round((v1(1)),3)),'   ,    ',num2str(round((v1(2)),3)),',    ',num2str(round((v1(3)),3)),',     1.00000    ,     0.00000    ,     0.00000\r\n'];
     line2 = [' ',num2str(round((v2(1)),3)),'   ,    ',num2str(round((v2(2)),3)),',    ',num2str(round((v2(3)),3)),',     0.00000    ,     0.00000    ,     1.00000\r\n'];
    M6 = ['50.,   0.001,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '20.,  402.5,    150.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1,      1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '0.,      0.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,      1.,      0.,      0.,      0.,      0.,      0.,      0.\r\n',...
          '1.,     10.,   1e-05,      0.,      0.,      0.,      0.,      0.\r\n    0.,    0.,      0,      0.,      0.,      0.,      0.,      0.\r\n'];
                 fprintf(file,M1);
                 fprintf(file,Mplus);
                 fprintf(file,M2);
                 fprintf(file,M3);
                 fprintf(file,M4);
                 fprintf(file,M5);
                 fprintf(file,line1);
                 fprintf(file,line2) ;
                 fprintf(file,M6);
    end
end
fclose(file);
end