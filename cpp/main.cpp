#include <iostream>
#include <string>
#include <algorithm>
#include <chrono>
#include <ctime>

#include "Piece.h"
#include "Grille.h"

const char* cl_pieces[9] = {"j", "j", "j", "o", "o", "r", "r", "n", "n"};
int gr[6][6] = {
    {0,0,0,0,-1,0},
    {-1,0,-1,0,0,-1},
    {0,0,0,-1,0,0},
    {0,-1,0,0,0,-1},
    {0,0,-1,0,0,0},
    {-1,0,0,0,0,-1}
};

int forbidden_cases_l[9][4][2] = {
    {{0, 3}, {3, 0}, {3, 3}, {-2,-2}}, //00
    {{0, 0}, {0, 3}, {3, 3}, {-2,-2}}, //01
    {{0, 0}, {0, 3}, {3, 3}, {-2,-2}}, //10
    {{0, 0}, {0, 3}, {3, 0}, {-2,-2}}, //11
    {{0, 0}, {3, 0}, {0, 3}, {-2,-2}}, //20
    {{0, 0}, {3, 0}, {3, 3}, {-2,-2}}, //21
    {{0, 0}, {3, 0}, {3, 3}, {-2,-2}}, //30
    {{3, 0}, {0, 3}, {3, 3}, {-2,-2}}  //31
 };

int forbidden_cases_t[4][2] = {{0,0}, {0,3}, {3,0}, {3, 3}};

int forbidden_cases_s[4][4][2] = {
        {{0,0}, {4,3}, {-2,-2}, {-2,-2}},   //00
        {{3,0}, {-1,3}, {-2,-2}, {-2,-2}},  //01
        {{3,0}, {0,4}, {-2,-2}, {-2,-2}},   //10
        {{0,0}, {3,4}, {-2,-2}, {-2,-2}}    //11
        };

using namespace std;

bool elt_in_list(int list[4][2], int xpos, int ypos, int lenlist){
    for (int i=0; i<lenlist; i++) {
        if (list[i][0] == xpos && list[i][1] == ypos){
            return true;
        }
    }

    return false;
}

void obtenir_ttes_possibilites(vector<Piece> ttes_pos[9], Grille grille){
    for (int pieceIdx=0;pieceIdx<9;pieceIdx++){
        const char* piece_coul = cl_pieces[pieceIdx];
        int rotnum = 4;
        bool flip[2] = {false, true};

        for (int rot=0;rot<rotnum;rot++){
            for (int xp=0;xp < (5-int(rot%2==1)); xp++){
                for (int yp=0;yp < (5-int(rot%2==0)); yp++){
                    for (int fl = 0; fl<2; fl++){
                        int xm = 0; 
                        int ym = 0;

                        if (rot == 0){
                            xm = -fl;
                        }
                        if (rot == 2){
                            xm = fl - 1;
                        }
                        if (rot == 3){
                            ym = 1;
                        }
                        int xpos = xp+xm; 
                        int ypos = yp-ym;

                        if ((piece_coul == "o") || (piece_coul == "r")){
                            
                            if (elt_in_list(forbidden_cases_l[rot*2+fl], xpos, ypos, 3)){
                                continue;
                            }
                        }
                        if (piece_coul == "n"){
                            if (elt_in_list(forbidden_cases_t, xpos, ypos, 4)){
                                continue;
                            }
                        }
                        if (piece_coul == "j"){
                            if (pieceIdx == 0){
                                //cout << "COULEUR: " << piece_coul << " POSX: " << xpos << " POSY: " << ypos << " ROT: " << rot << " FLIP?: " << fl << endl;
                                Piece pic = Piece(pieceIdx, xpos, ypos, rot, fl);
                                //pic.afficher();
                            }
                            if (elt_in_list(forbidden_cases_s[(rot)%2*2+fl], xpos, ypos, 2)){

                                //Piece pic = Piece(pieceIdx, xpos, ypos, rot, fl);
                                //cout << "THIS DEOSNT WORK vvv"<<endl;
                                //pic.afficher();
                                continue;
                            }
                        }
                        Piece pic = Piece(pieceIdx, xpos, ypos, rot, fl);
                        if (piece_coul == "o"){
                            //cout << "COULEUR: " << piece_coul << " POSX: " << xpos << " POSY: " << ypos << " ROT: " << rot << " FLIP?: " << fl << endl;
                        
                            //pic.afficher();
                        }
                        if (grille.verif_smileys(pic)){
                            ttes_pos[pieceIdx].push_back(pic);
                        }
                    }
                }
            }
        }
    }
}

int remplir_grille(Grille grille, vector<Piece> ttes_pos[9]){
    int p = 0;
    int piece_idx = grille.piece_manquante_dernier();
    
    for (Piece piece_test : ttes_pos[piece_idx]){

        if (grille.verifier(piece_test)){
            grille.ajouter(piece_test);
            grille.mettre_dans_grille(piece_test);
            
            if (grille.pieces.size() == 9){
                //cout << "GRILLE COMPLETE§!!!!!!!!!!" << endl;
                return p+1;
            }
            else{
                
                //grille.afficher();
                p+= remplir_grille(grille, ttes_pos);
            }
            grille.retirer_dernier(piece_idx);
        }

    }
    return p;
}

int main(int argc, char *argv[]){
    
    vector<Piece> ttes_pos[9] = {};
    
    Grille g(gr);
    
    obtenir_ttes_possibilites(ttes_pos, gr);

    
    auto start = chrono::system_clock::now();
    int num = remplir_grille(g, ttes_pos);

    auto end = std::chrono::system_clock::now();
    chrono::duration<double> elapsed_seconds = end-start;

    cout << num << " solutions found in "<< elapsed_seconds.count() << "s"
              << endl;
    return 0;
}