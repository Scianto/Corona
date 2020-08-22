#corona v1.2
#author:sci_anto
#https://github.com/Scianto/Corona
print("""
\033[1;31m
  ██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗ █████╗            
 ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗████╗  ██║██╔══██╗   
 ██║     ██║   ██║██████╔╝██║   ██║██╔██╗ ██║███████║           
 ██║     ██║   ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║          
 ╚██████╗╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║      
  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝            
                                                      """)    
from covid import Covid
covid = Covid()
cases = covid.get_status_by_country_name("india") 
for x in cases:
       print(x, ":",cases[x])
