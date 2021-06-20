# coding: UTF-8

from core.StatusInvest import StatusInvest
from core.Pichau import Pichau
from core.Kabum import Kabum
import sys


def main(choice):

    if choice == 1:
        pichau_links = open("pichau.txt", "r").readlines()

        for link in pichau_links:
            pichau = Pichau(link)
            pichau.start()
            result = pichau.finish()

            print(result)

    elif choice == 2:
        kabum_links = open("kabum.txt", "r").readlines()

        for link in kabum_links:
            kabum = Kabum(link)
            kabum.start()
            result = kabum.finish()

            print(result)

    elif choice == 3:
        tickers = sys.argv[2::]

        status_invest = StatusInvest(tickers)
        status_invest.start()
        result = status_invest.finish()

        print(result)


if __name__ == "__main__":
    print(
        """
                                                                                            
                                                                                            
   SSSSSSSSSSSSSSS                           iiii          tttt         hhhhhhh             
 SS:::::::::::::::S                         i::::i      ttt:::t         h:::::h             
S:::::SSSSSS::::::S                          iiii       t:::::t         h:::::h             
S:::::S     SSSSSSS                                     t:::::t         h:::::h             
S:::::S               mmmmmmm    mmmmmmm   iiiiiiittttttt:::::ttttttt    h::::h hhhhh       
S:::::S             mm:::::::m  m:::::::mm i:::::it:::::::::::::::::t    h::::hh:::::hhh    
 S::::SSSS         m::::::::::mm::::::::::m i::::it:::::::::::::::::t    h::::::::::::::hh  
  SS::::::SSSSS    m::::::::::::::::::::::m i::::itttttt:::::::tttttt    h:::::::hhh::::::h 
    SSS::::::::SS  m:::::mmm::::::mmm:::::m i::::i      t:::::t          h::::::h   h::::::h
       SSSSSS::::S m::::m   m::::m   m::::m i::::i      t:::::t          h:::::h     h:::::h
            S:::::Sm::::m   m::::m   m::::m i::::i      t:::::t          h:::::h     h:::::h
            S:::::Sm::::m   m::::m   m::::m i::::i      t:::::t    tttttth:::::h     h:::::h
SSSSSSS     S:::::Sm::::m   m::::m   m::::mi::::::i     t::::::tttt:::::th:::::h     h:::::h
S::::::SSSSSS:::::Sm::::m   m::::m   m::::mi::::::i     tt::::::::::::::th:::::h     h:::::h
S:::::::::::::::SS m::::m   m::::m   m::::mi::::::i       tt:::::::::::tth:::::h     h:::::h
 SSSSSSSSSSSSSSS   mmmmmm   mmmmmm   mmmmmmiiiiiiii         ttttttttttt  hhhhhhh     hhhhhhh
                                                                                            
                                                                                            
    """
    )

    try:
        choice = int(sys.argv[1])
    except IndexError:
        print("Help: [1] Pichau / [2] Kabum / [3] Status Invest")

    main(choice)
