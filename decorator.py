def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx()
        print("Thanks for using")
    return mfx
    
@greet
def hello():
    print("Hello world")

hello()
# greet(hello)()