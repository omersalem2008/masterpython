# -------------------------------------------------
# -- Advanced_Lessons => __name__ And "__main__" --
# -------------------------------------------------
# if __name__ == "__main__":
# - __name__ => Built In Variable
# - "__main__" => Value Of The __name__ Variable
# Executions Methods
# - Directly => Execute the Python File Using the Command Line.
# - From Import => Import The Code From File To Another File
# -------------------------------------------------------------
# In Some Cases You Want To Know If You Are Using A Module Method As Import
# Or You Use The Original Python File
# -------------------------------------------------------------------------
# In Direct Mode Python Assign A Value "__main__"
# To The Built In Variable __name__ in The Background
# ---------------------------------------------------
from py2 import *
# so here after run this file then it will show everything on py2.py 
#except the message that is inside the if __name__ == "__main__":
# because this message will be displayed only when the file 
# is executed directly so the result will be:
# "this message will be displayed for everyone"
print(__name__)