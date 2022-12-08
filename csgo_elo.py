version = '1.1.1'
changelog = 'change.log'

import math
import sys
import tkinter as tk

def show_exception_and_exit(exc_type, exc_value, tb):
    if not exc_type == KeyboardInterrupt:
        import traceback
        traceback.print_exception(exc_type, exc_value, tb)
        input("Press ENTER to exit...")
        sys.exit(-1)
        
sys.excepthook = show_exception_and_exit

class input_and_validate:
    def _int(vmin, vmax, prompt=None, message=None):
        in1 = int(input(prompt))
        while in1 < vmin or in1 > vmax:
            if message == None:
                print("Input should be an integer in the range "+str(vmin)+"-"+str(vmax))
            else:
                print(message)
            in1 = int(input(prompt))
        return in1
        

# Silver 1 has a floor of 0
# Global Elite has a ceiling of 1900

class sg2toRank:
    def rank(sg2):
        if sg2 >= 0 and sg2 < 100:
            return 'Silver 1'
        elif sg2 >= 100 and sg2 < 200:
            return 'Silver 2'
        elif sg2 >= 200 and sg2 < 300:
            return 'Silver 3'
        elif sg2 >= 300 and sg2 < 400:
            return 'Silver 3'
        elif sg2 >= 400 and sg2 < 500:
            return 'Silver 4'
        elif sg2 >= 500 and sg2 < 600:
            return 'Silver Elite'
        elif sg2 >= 600 and sg2 < 700:
            return 'Silver Elite Master'
        elif sg2 >= 700 and sg2 < 800:
            return 'Gold Nova 1'
        elif sg2 >= 800 and sg2 < 900:
            return 'Gold Nova 2'
        elif sg2 >= 900 and sg2 < 1000:
            return 'Gold Nova 3'
        elif sg2 >= 1000 and sg2 < 1100:
            return 'Gold Nova Master'
        elif sg2 >= 1100 and sg2 < 1200:
            return 'Master Guardian 1'
        elif sg2 >= 1200 and sg2 < 1300:
            return 'Master Guardian 2'
        elif sg2 >= 1300 and sg2 < 1400:
            return 'Master Guardian Elite'
        elif sg2 >= 1400 and sg2 < 1500:
            return 'Distinguished Master Guardian'
        elif sg2 >= 1500 and sg2 < 1600:
            return 'Legendary Eagle'
        elif sg2 >= 1600 and sg2 < 1700:
            return 'Legendary Eagle Master'
        elif sg2 >= 1700 and sg2 < 1800:
            return 'Supreme Master First Class'
        elif sg2 >= 1800 and sg2 <= 1900:
            return 'Global Elite'
        else:
            raise Exception("Invalid SG2 value Expected: integer in range 0-1900 Recieved: "+str(sg2))

    def main():
        root.destroy()
        in1 = input_and_validate._int(0,1900,"Enter SG2 value: ")
        print("An SG2 value of", in1, "means a rank of", sg2toRank.rank(in1))
        main()

# The team elo is calculated using a numerical identifier
# Silver 1 = 1
# Global Elite = 18

class elo_calculation:
    def elo_calc(Ys,Os,M,Oe,Ye,s):
        return (((5*(Ys-Os))/3)+M+(Oe-Ye))*(1-math.log(s,16))
    def main():
        root.destroy()
        score = input_and_validate._int(0,16,"Your round wins: ")
        e_score = input_and_validate._int(0,16,"Opponent round wins: ")
        mvp = input_and_validate._int(0,score,"MVPs: ","You cannot have more MVPs than your team's round wins")
        e_elo = input_and_validate._int(0,90,"Approximate elo of enemy team: ")
        elo = input_and_validate._int(0,90,"Approximate elo of your team: ")
        win_loss = int(input("Win/Loss streak: "))
        sigma = 0
        if win_loss > 0:
            sigma = win_loss
        elif win_loss >= -4 and win_loss < 0:
            if win_loss == -1:
                sigma = 1/16
            elif win_loss == -2:
                sigma = 1/8
            elif win_loss == -3:
                sigma = 1/4
            elif win_loss == -4:
                sigma = 1/2
        elif win_loss < -4:
            sigma = (0 - win_loss) - 4
        else:
            raise Exception("Win/Loss streak should be inputted as a positive integer for a winstreak or a negative integer for a loss streak")
        print("Estimated elo gain =", elo_calculation.elo_calc(score,e_score,mvp,e_elo,elo,sigma))
        main()

def exit_program():
    root.destroy()
    sys.exit(0)


def main():
    print("Use the menu to select an option")
    global root
    root= tk.Tk()
    root.title("CS:GO Elo calculator ("+version+")")
    root.config(bg='#FFFFFF')
    frame = tk.Frame(
        master=root,
        bg='#FFFFFF'
    )
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    label = tk.Label(
        master=frame,
        text="Select an option",
        height=1,
        width=40,
        bg='#FFFFFF'
    )
    
    calc_button = tk.Button(
        master=frame,
        text="Calculate Elo gain",
        height=1,
        width=20,
        bg='#FFFFFF',
        command=elo_calculation.main
    )
    
    conv_button = tk.Button(
        master=frame,
        text="SG2 to Rank converter",
        height=1,
        width=20,
        bg='#FFFFFF',
        command=sg2toRank.main
    )

    exit_button = tk.Button(
        master=frame,
        text="Exit",
        height=1,
        width=5,
        bg='#FFFFFF',
        command=exit_program
    )

    label.pack(side=tk.TOP, fill=tk.BOTH, pady=4)
    exit_button.pack(side=tk.BOTTOM, fill=tk.Y, pady=1, padx=4)

    calc_button.pack(side=tk.LEFT, fill=tk.BOTH, padx=4, pady=4)
    conv_button.pack(side=tk.RIGHT, fill=tk.BOTH, padx=4, pady=4)

    root.eval('tk::PlaceWindow . center')

    root.mainloop()

main()

