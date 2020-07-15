from game import variables as vs
class Scoreboard():

    def score(self,a,b):
        s=f"______________________________________\n" \
          "----------scoreboard-------------------\n" \
          "{a}={vs.p1}\n" \
          "{b}={vs.p2}\n" \
          "_________________________________________"
        return s
            # return vs.p2
