#include <iostream>
#include <algorithm>
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
            retourner(r);
            if (f){
                flipper();
            }
                
            switch (coul){
                case "j": 
                    clr = {237, 212, 70, 255};
                    break;
                case "n": 
                    clr = {95, 95, 95, 255};
                    break;
                case "r": 
                    clr = {204, 54, 54, 255};
                    break;
                case "o": 
                    clr = {228, 142, 42, 255};
                    break;

            }
                
        }
        void retourner(int rotIdx){
            rotate(piece[0], piece[1]+1, piece[3]+3);
            rot += rotIdx;
            }
                
        void flipper(){

            for (int i=0;i<3;i++)
            {
                reverse(piece[i], piece[i]+3);
            }
            flip = !flip;
        }
        

};