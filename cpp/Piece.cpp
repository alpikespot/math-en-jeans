#include <iostream>
#include <algorithm>
#include <cstring>
#include "Piece.h"
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



 Piece::Piece(int indx, int px, int py, int r, bool f){
    
    copy(tt_pieces[indx][0], tt_pieces[indx][0]+3, piece[0]);
    copy(tt_pieces[indx][1], tt_pieces[indx][1]+3, piece[1]);
    copy(tt_pieces[indx][2], tt_pieces[indx][2]+3, piece[2]);
    
    const char* coul = c_pieces[indx];
    p_x = px;
    p_y = py;
    piece_idx = indx;
    for (int rep=0;rep<r;rep++){
        retourner();
    }
    
    if (f){
        flipper();
    }
    
    /*   
    if (coul == "j")
        {clr = {237, 212, 70, 255};}

        case "n": 
            clr = {95, 95, 95, 255};
            break;
        case "r": 
            clr = {204, 54, 54, 255};
            break;
        case "o": 
            clr = {228, 142, 42, 255};
            break;*/ 

    
        
}

void Piece::retourner(){
    int rotIdx=1;
    int new_piece[3][3];
    //rotate(piece[0], piece[0], piece[0]);
    rot += rotIdx;
    //cout << "ROTIDX: " << rotIdx << endl;
        //int new_piece[3][3]= {{0,0,0},{0,0,0},{0,0,0}};
        //cout << "ROTATED" << endl;
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                new_piece[i][j] = piece[2-j][i];
            }
        }
    
        memcpy(piece, new_piece, sizeof(int)*9);
}
        
void Piece::flipper(){

    for (int i=0;i<3;i++)
    {
        reverse(piece[i], piece[i]+3);
    }
    flip = !flip;
}

bool Piece::verifier(int grille[6][6]){
    for (int y=0;y<3;y++)
    {
        for (int x=0;x<3;x++)
        {
            if (piece[y][x] > 0)
            {
                if (( !(0<=(y+p_y)<=5) || !(0<=(x+p_x)<=5)) || grille[y+p_y][x+p_x] > 0)

                    {
                        return false;
                    }
            }
                
        }
    }
    return true;
}

void Piece::afficher(){
    for (int y=0;y<3;y++){
        for (int x=0;x<3;x++){
            if (piece[y][x] >= 1)
            {cout<<"# ";}
            else
            {cout << "  ";}
            
        }
        cout << endl;
    }
        
}
        

