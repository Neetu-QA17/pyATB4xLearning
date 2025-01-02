# Re-initialization of the public variable in a function - preference will be given to local variable
# Local variable has more preference than public variable

public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"
    print(public_toilet)

def strange():
    print(public_toilet)
#    print(private_toilet)

home()
strange()
