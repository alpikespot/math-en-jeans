#include "Piece.h"
#include "Grille.h"
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

Grille::Grille(int gr[6][6]){
    memcpy(grille, gr, sizeof(int)*6*6);
    memcpy(grille_originale, gr, sizeof(int)*6*6);

}
const char* grille_symbols[4] = {"o", " ", "#", "X"};
void Grille::afficher(){
    cout << "GRILLE: "<< endl;
    for (int y=0;y<6;y++){
        cout << "| ";
        for (int x=0;x<6;x++){

            cout << grille_symbols[grille[y][x]+1] << " ";

        }
        cout << "|" << endl;
    }
    cout << endl;
}

void Grille::ajouter(Piece piece_aj){
    mettre_dans_grille(piece_aj);
    pieces.push_back(piece_aj);
}

bool Grille::verifier(Piece piece_test){
    for (int y=0;y<3;y++){
        for (int x=0;x<3;x++){
            int posy = piece_test.p_y + y;
            int posx = piece_test.p_x + x;
            if (piece_test.piece[y][x] != 0){
                if (!(0<=posx<=5 && 0<=posy<=5)){
                    return false;
                }
                else if (grille[posy][posx] >= 1 ){
                    return false;
                }
            }
        }
    }
    return true;
}

bool Grille::verif_smileys(Piece piece_test){
    for (int y=0;y<3;y++){
        for (int x=0;x<3;x++){
            int posy = piece_test.p_y + y;
            int posx = piece_test.p_x + x;
            if (piece_test.piece[y][x] >= 1){
                if ((grille_originale[posy][posx] == -1) != (piece_test.piece[y][x] == 2)){ //si seul un de ces expressions est vraie
                    return false;
                }
            }               
        }
    }
    return true;
}

bool Grille::verif_complete(){
    for (int y=0;y<6;y++){
        for (int x=0;x<6;x++){
            if (grille[y][x] <= 0){
                return false;
            }

        }
    }
    return true;
}

void Grille::mettre_dans_grille(Piece piece_aj){
    for (int y=0;y<3;y++){
        for (int x=0;x<3;x++){
            int p_x = piece_aj.p_x + x; 
            int p_y = piece_aj.p_y + y;

            if (piece_aj.piece[y][x] > 0){
                if (grille[p_y][p_x] <= 0){
                    grille[p_y][p_x] = piece_aj.piece[y][x];
                }
                    
            }
        }
    }
}

void Grille::retirer_dernier(int idx){
    int i=0;
    Piece *piece_ret;

    for(Piece pc : pieces) {

        if (pc.piece_idx == idx){
            piece_ret = &pc;
            break;
        }
        i++; 
        
    }

    for (int y=0;y<3;y++){
        for (int x=0;x<3;x++){
            int posy = piece_ret->p_y + y;
            int posx = piece_ret->p_x + x;

            if ((0<=posx<=5 and 0<=posy<=5) && (piece_ret->piece[y][x]) >= 1){
                grille[posy][posx] = grille_originale[posy][posx];
            }
                
        }
    }
    pieces.erase(pieces.begin()+i);

}

int Grille::piece_manquante_dernier(){
    vector<int> piece_manq{0,1,2,3,4,5,6,7,8};
    //int piece_manq[9] = {0,1,2,3,4,5,6,7,8};

    for (Piece piece :pieces){
        for (int i=0; i<sizeof(piece_manq)/sizeof(int); i++){
            if (piece.piece_idx == piece_manq[i]){
                piece_manq.erase(piece_manq.begin()+i);
                break;
            }
        }
        //piece_manq.erase(remove(piece_manq.begin(), piece_manq.end(), piece.piece_idx), piece_manq.end());
        //piece_manq.erase(piece_manq.begin()+5);
        //piece_manq.remove(piece.idx)
    }
    return piece_manq[0];

}
