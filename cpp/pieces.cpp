#include <iostream>
using namespace std;

const char* c_pieces[9] = {"j", "j", "j", "o", "o", "r", "r", "n", "n"};
const int tt_pieces[9][3][3] = {
 {{0,2,0}, //les jaunes
  {2,1,0},
  {1,0,0}},
 
 {{0,2,0},
  {1,1,0},
  {1,0,0}},

{{0,1,0},
 {2,1,0},
 {1,0,0}},

{{1,1,0}, //les oranges
 {0,2,0},
 {0,1,0}},
 
 {{1,2,0},
  {0,1,0},
  {0,1,0}},

 {{2,1,0}, //les rouges
  {0,1,0},
  {0,1,0}},

 {{1,1,0},
  {0,1,0},
  {0,2,0}},

 {{0,1,0}, //les noires
  {2,1,0},
  {0,1,0}},
 
 {{0,2,0},
  {1,1,0},
  {0,1,0}}
 
 };

class Piece{
    
    public:
        int piece[3][3] = {0};
        char clr[4] = {0,0,0,255};
        int x, y, idx;
        int rot = 0;
        bool flip = false;

        Piece(int indx, int px=0, int py=0, int r=0,bool f = false){
            
            copy(tt_pieces[indx], tt_pieces[indx]+9, piece);
            const char* coul = c_pieces[indx];
            x = px;
            y = py;
            idx = indx;
            self.retourner(r)
            #print(self.piece)
            if (f){
                self.flipper()
            }
                
            match coul:
                case "j": self.clr = np.array([237, 212, 70, 255])
                case "n": self.clr = np.array([95, 95, 95, 255])
                case "r": self.clr = np.array([204, 54, 54, 255])
                case "o": self.clr = np.array([228, 142, 42, 255])
        }

};